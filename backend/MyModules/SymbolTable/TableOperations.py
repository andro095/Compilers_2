from .Table import SymbolTable, TableItem
from .Constants import constants
from YAPL import YaplParser
from utils import indx
from antlr4 import ParserRuleContext
from ConsoleMessages import MessagesDB
from Global import global_constants


#TODO: Actualizar el tamaño de los let
class TableOperations:
    def __init__(self) -> None:
        self.symbol_table = SymbolTable()
        self.msgs_db = MessagesDB()
    
    def get_ctx_attr(self, ctx: ParserRuleContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        line = (ctx.children[0].symbol.line, ctx.children[0].symbol.column)
        
        return children, line
    
    def get_class_byte_size(self, class_name: str) -> int:
        for symbol in self.symbol_table.tables[0].items:
            if symbol.lex == class_name:
                return symbol.byte_size
            
        return -1
    
    def insert_self(self, line: tuple[int, int]):
        
        table_item = TableItem(
            lex=constants.string_literals.SELF,
            token=global_constants.token_types.ID,
            typ=self.symbol_table.tables[self.symbol_table.actual_scope].name,
            line=line,
            sem_kind=global_constants.sem_kinds.ATTR,
            param_method=constants.param_methods.REF,
            byte_size=global_constants.byte_size.CLASS
        )
        return self.symbol_table.insert(table_item)
        
    def insert_class(self, ctx: YaplParser.ClassContext) -> bool:
        children, line = self.get_ctx_attr(ctx)
        ind = indx(children, constants.string_literals.INHERITS[0])
        if ind == -1:
            ind = indx(children, constants.string_literals.INHERITS[1])
            
        if ind != -1 and children[ind + 1] in global_constants.BASIC_TYPES:
            self.msgs_db.insert_error(line, f'La clase {children[1]} no puede heredar de {children[ind + 1]}.')
            return False
            
        if ind != -1 and children[ind + 1] == children[1]:
            self.msgs_db.insert_error(line, f'La clase {children[1]} no puede heredar de si misma.')
            return False
        
        byte_size = global_constants.byte_size.CLASS
        
        if ind != -1:
            class_size = self.get_class_byte_size(children[ind + 1])
            if class_size == -1:
                self.msgs_db.insert_error(line, f'La clase {children[ind + 1]} no ha sido declarada.')
                return False
            byte_size += class_size
           
        table_item = TableItem(
            lex=children[1],
            token=ctx.children[1].symbol.type,
            inherits=children[ind + 1] if ind != -1 else global_constants.basic_types.OBJECT if children[1] != constants.string_literals.MAIN else None,
            line=line,
            sem_kind=global_constants.sem_kinds.CLASS,
            param_method=constants.param_methods.REF,
            byte_size=byte_size        
        )
        
        return self.symbol_table.insert(table_item)
    
    def insert_feature(self, ctx: YaplParser.FeatureContext) -> bool:
        children, line = self.get_ctx_attr(ctx)
        ind = indx(children, global_constants.string_cons.TYPE_DELIMITER)
        sem_kind = global_constants.sem_kinds.METHOD if children[1] != global_constants.string_cons.TYPE_DELIMITER else global_constants.sem_kinds.ATTR    
        param_num = 0
        byte_size = 0
        
        if sem_kind == global_constants.sem_kinds.METHOD:
            cround = indx(children, constants.string_literals.CROUND)
            param_num = len(list(filter(lambda x: x != constants.string_literals.COMMA, children[2:cround])))
       
        if children[ind + 1].lower() == global_constants.basic_types.INT.lower():
            byte_size = global_constants.byte_size.INT
        elif children[ind + 1].lower() == global_constants.basic_types.BOOL.lower():
            byte_size = global_constants.byte_size.BOOL
        elif children[ind + 1].lower() == global_constants.basic_types.STRING.lower():
            byte_size = global_constants.byte_size.STRING
        else:
            table_name = self.symbol_table.tables[self.symbol_table.actual_scope].name
            if children[ind + 1] == table_name or children[ind + 1] == global_constants.basic_types.SELF_TYPE:
                byte_size = global_constants.byte_size.CLASS
            else:
                byte_size = self.get_class_byte_size(children[ind + 1])
        
        
        table_item = TableItem(
            lex=children[0],
            token=ctx.children[0].symbol.type,
            typ=children[ind + 1] if children[ind + 1] != global_constants.basic_types.SELF_TYPE else self.symbol_table.tables[self.symbol_table.actual_scope].name,
            line=line,
            sem_kind=sem_kind,
            param_method=constants.param_methods.REF,
            param_num=param_num,
            byte_size=byte_size
        )
        return self.symbol_table.insert(table_item)
        
        

        
    def insert_formal(self, ctx: YaplParser.FormalContext) -> bool:
        children, line = self.get_ctx_attr(ctx)
        
        print(f'Scope: {self.symbol_table.tables[self.symbol_table.scopes[-2]].name}, Lex: {children[0]}, Type: {children[2]}')
        
        byte_size = 0
        
        if children[2].lower() == global_constants.basic_types.INT.lower():
            byte_size = global_constants.byte_size.INT
        elif children[2].lower() == global_constants.basic_types.BOOL.lower():
            byte_size = global_constants.byte_size.BOOL
        elif children[2].lower() == global_constants.basic_types.STRING.lower():
            byte_size = global_constants.byte_size.STRING
        
        table_index = self.symbol_table.get_table_index(self.symbol_table.tables[self.symbol_table.scopes[-2]].name)
        lex_name = self.symbol_table.tables[self.symbol_table.actual_scope].name
        
        self.symbol_table.add_byte_size(table_index, lex_name, byte_size)
        
        
        table_item = TableItem(
            lex=children[0],
            token=ctx.children[0].symbol.type,
            typ=children[2],
            line=line,
            sem_kind=global_constants.sem_kinds.PARAMETER,
            param_method=constants.param_methods.REF,
            byte_size=byte_size
        )
        
        return self.symbol_table.insert(table_item)
        
    def insert_expr(self, ctx: YaplParser.ExprContext) -> bool:
        children, line = self.get_ctx_attr(ctx)
        
        if children[0].lower() == global_constants.string_cons.LET:
            param_num = len(list(filter(lambda x: x == global_constants.string_cons.TYPE_DELIMITER, children[2:-1])))
            table_item = TableItem(
                lex=global_constants.string_cons.LET + str(self.symbol_table.lets_counter),
                token=ctx.children[1].symbol.type,
                line=line,
                sem_kind=global_constants.sem_kinds.EXPR,
                param_num=param_num
            )
            inserted = self.symbol_table.insert(table_item)
            
            if inserted:
                self.symbol_table.push_scope(global_constants.string_cons.LET + str(self.symbol_table.lets_counter))
                self.symbol_table.lets_counter += 1
                
                type_delimiter_indexes = []
                for i in range(len(children)):
                    if children[i] == global_constants.string_cons.TYPE_DELIMITER:
                        type_delimiter_indexes.append(i)
                        
                for i in type_delimiter_indexes:
                    table_item = TableItem(
                        lex=children[i - 1],
                        token=ctx.children[i - 1].symbol.type,
                        typ=children[i + 1],
                        line=line,
                        sem_kind=global_constants.sem_kinds.ATTR,
                        param_method=constants.param_methods.REF
                    )
                    self.symbol_table.insert(table_item)
                
                self.symbol_table.pop_scope()
    
            return inserted
    