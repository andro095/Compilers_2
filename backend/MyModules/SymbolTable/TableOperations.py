from .Table import SymbolTable, TableItem
from .Constants import constants, types
from YAPL import YaplParser
from utils import indx
from antlr4 import ParserRuleContext
from ConsoleMessages import MessagesDB

# TODO: Agregar el tipo de retorno de la funciones
class TableOperations:
    def __init__(self) -> None:
        self.symbol_table = SymbolTable()
        self.msgs_db = MessagesDB()
        
    def assign_value(self, ctx: YaplParser.ExprContext):
        self.symbol_table.set(ctx.children[0].getText(), ctx.children[0].symbol.line, ctx.children[2].getText())
    
    def get_ctx_attr(self, ctx: ParserRuleContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        line = (ctx.children[0].symbol.line, ctx.children[0].symbol.column)
        
        return children, line
    
    def insert_self(self, line: tuple[int, int]):
        
        table_item = TableItem(
            lex=constants.SELF,
            token=types.ID,
            typ=constants.SELF_TYPE,
            line=line,
            sem_kind=constants.ATTR,
            param_method=constants.REF
        )
        self.symbol_table.insert(table_item)
        
    def insert_class(self, ctx: YaplParser.ClassContext):
        children, line = self.get_ctx_attr(ctx)
        ind = indx(children, constants.INHERITS[0])
        if ind == -1:
            ind = indx(children, constants.INHERITS[1])
            
        if ind != -1 and children[ind + 1] in constants.BASIC_TYPES:
                self.msgs_db.insert_error(line, f'La clase {children[1]} no puede heredar de {children[ind + 1]}')
                return
           
        table_item = TableItem(
            lex=children[1],
            token=ctx.children[1].symbol.type,
            inherits=children[ind + 1] if ind != -1 else constants.types.OBJECT if children[1] != constants.MAIN else None,
            line=line,
            sem_kind=constants.CLASS,
            param_method=constants.REF            
        )
        
        self.symbol_table.insert(table_item)
    
    def insert_feature(self, ctx: YaplParser.FeatureContext):
        children, line = self.get_ctx_attr(ctx)
        ind = indx(children, constants.TYPE_DELIMITER)
        sem_kind = constants.METHOD if children[1] != constants.TYPE_DELIMITER else constants.ATTR    
        param_num = 0
        
        if sem_kind == constants.METHOD:
            cround = indx(children, constants.CROUND)
            param_num = len(list(filter(lambda x: x != constants.COMMA, children[2:cround])))
        
        
        table_item = TableItem(
            lex=children[0],
            token=ctx.children[0].symbol.type,
            typ=children[ind + 1],
            line=line,
            sem_kind=sem_kind,
            param_method=constants.REF,
            param_num=param_num
        )
        insert_res = self.symbol_table.insert(table_item)
        
        if sem_kind == constants.METHOD and insert_res is None:
            print("Empujando scope", children[0])
            self.symbol_table.push_scope(children[0])
        

        
    def insert_formal(self, ctx: YaplParser.FormalContext):
        children, line = self.get_ctx_attr(ctx)
        
        table_item = TableItem(
            lex=children[0],
            token=ctx.children[0].symbol.type,
            typ=children[2],
            line=line,
            sem_kind=constants.PARAMETER,
            param_method=constants.REF,
        )
        
        self.symbol_table.insert(table_item)
        
    def insert_expr(self, ctx: YaplParser.ExprContext):
        children, line = self.get_ctx_attr(ctx)
        
        print(children)
        
        if children[0].lower() == constants.LET:
            param_num = len(list(filter(lambda x: x == constants.TYPE_DELIMITER, children[2:-1])))
            table_item = TableItem(
                lex=constants.LET + str(self.symbol_table.lets_counter),
                token=ctx.children[1].symbol.type,
                line=line,
                sem_kind=constants.EXPR,
                param_num=param_num
            )
            self.symbol_table.insert(table_item)
            self.symbol_table.push_scope(constants.LET + str(self.symbol_table.lets_counter))
            self.symbol_table.lets_counter += 1
            
            type_delimiter_indexes = []
            for i in range(len(children)):
                if children[i] == constants.TYPE_DELIMITER:
                    type_delimiter_indexes.append(i)
                    
            for i in type_delimiter_indexes:
                table_item = TableItem(
                    lex=children[i - 1],
                    token=ctx.children[i - 1].symbol.type,
                    typ=children[i + 1],
                    line=line,
                    sem_kind=constants.ATTR,
                    param_method=constants.REF
                )
                self.symbol_table.insert(table_item)
            
            self.symbol_table.pop_scope()
    
    
    @property
    def table(self) -> SymbolTable:
        return self.symbol_table
    