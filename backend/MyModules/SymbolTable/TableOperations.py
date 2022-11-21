from .Table import SymbolTable, TableItem
from .Constants import constants
from YAPL import YaplParser
from utils import indx
from antlr4 import ParserRuleContext
from ConsoleMessages import MessagesDB
from .Table import MemoryCounters
from Global import global_constants

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
            byte_size=global_constants.byte_size.CLASS,
            mem_base=global_constants.base_memory.HEAP
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
           
        table_item = TableItem(
            lex=children[1],
            token=ctx.children[1].symbol.type,
            inherits=children[ind + 1] if ind != -1 else global_constants.basic_types.OBJECT if children[1] != constants.string_literals.MAIN else None,
            line=line,
            sem_kind=global_constants.sem_kinds.CLASS,
            param_method=constants.param_methods.REF,
            byte_size=byte_size        
        )
        
        inserted = self.symbol_table.insert(table_item)
        
        if inserted:
            self.symbol_table.class_memories[children[1]] = MemoryCounters()
        
        return inserted
    
    def insert_feature(self, ctx: YaplParser.FeatureContext) -> bool:
        children, line = self.get_ctx_attr(ctx)
        ind = indx(children, global_constants.string_cons.TYPE_DELIMITER)
        sem_kind = global_constants.sem_kinds.METHOD if children[1] != global_constants.string_cons.TYPE_DELIMITER else global_constants.sem_kinds.ATTR    
        param_num = 0
        byte_size = 0
        mem_base = global_constants.base_memory.HEAP
        
        if sem_kind == global_constants.sem_kinds.METHOD:
            cround = indx(children, constants.string_literals.CROUND)
            param_num = len(list(filter(lambda x: x != constants.string_literals.COMMA, children[2:cround])))
            mem_base = global_constants.base_memory.STACK
       
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
            byte_size=byte_size,
            mem_base=mem_base
        )
        return self.symbol_table.insert(table_item)
        
        

        
    def insert_formal(self, ctx: YaplParser.FormalContext) -> bool:
        children, line = self.get_ctx_attr(ctx)
        
        # print(f'Scope: {self.symbol_table.tables[self.symbol_table.scopes[-2]].name}, Lex: {children[0]}, Type: {children[2]}')
        
        byte_size = 0
        
        if children[2].lower() == global_constants.basic_types.INT.lower():
            byte_size = global_constants.byte_size.INT
        elif children[2].lower() == global_constants.basic_types.BOOL.lower():
            byte_size = global_constants.byte_size.BOOL
        elif children[2].lower() == global_constants.basic_types.STRING.lower():
            byte_size = global_constants.byte_size.STRING
        
        class_name = self.symbol_table.tables[self.symbol_table.scopes[1]].name
        self.symbol_table.add_class_size(class_name, byte_size)
        
        
        table_item = TableItem(
            lex=children[0],
            token=ctx.children[0].symbol.type,
            typ=children[2],
            line=line,
            sem_kind=global_constants.sem_kinds.PARAMETER,
            param_method=constants.param_methods.REF,
            byte_size=byte_size,
            mem_base=global_constants.base_memory.STACK
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

            return self.symbol_table.insert(table_item)
        
    
    
    def insert_let_param(self, ctx: YaplParser.ExprContext, i: int) -> bool:
        children, line = self.get_ctx_attr(ctx)
        table_item = TableItem(
            lex=children[i - 1],
            token=ctx.children[i - 1].symbol.type,
            typ=children[i + 1],
            line=line,
            sem_kind=global_constants.sem_kinds.PARAMETER,
            param_method=constants.param_methods.REF,
            mem_base=global_constants.base_memory.STACK,
            byte_size=self.symbol_table.get_byte_size(children[i + 1])
        )
        
        class_name = self.symbol_table.tables[self.symbol_table.scopes[1]].name
        self.symbol_table.add_class_size(class_name, table_item.byte_size)
        return self.symbol_table.insert(table_item)
    
    def insert_obj(self, ctx: YaplParser.ExprContext) -> bool:
        children, line = self.get_ctx_attr(ctx)
        
        exists_type = self.symbol_table.exists_in_table(0, children[1])
        
        if exists_type:        
            table_item = TableItem(
                lex=f'obj{self.symbol_table.objects_counter}',
                token=ctx.children[1].symbol.type,
                typ=children[1],
                line=line,
                sem_kind=global_constants.sem_kinds.OBJ,
                param_method=constants.param_methods.REF,
                mem_base=self.symbol_table.get_mem_base(ctx),
                byte_size=self.symbol_table.get_byte_size(children[1])
            )
            
            self.symbol_table.objects_counter += 1
            
            class_name = self.symbol_table.tables[self.symbol_table.scopes[1]].name
            self.symbol_table.add_class_size(class_name, table_item.byte_size)
            
            return self.symbol_table.insert(table_item)
        else:
            self.msgs_db.insert_error(line, f'El tipo {children[1]} no existe', global_constants.phase_error.SEMANTIC)
            
            return False