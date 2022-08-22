from .Table import SymbolTable, TableItem
from .Constants import constants, types
from YAPL import YaplParser
from utils import indx
from antlr4 import ParserRuleContext

class TableOperations:
    def __init__(self, symbol_table: SymbolTable) -> None:
        self.symbol_table: SymbolTable = symbol_table
        
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
        table_item = TableItem(
            lex=children[1],
            token=ctx.children[1].symbol.type,
            inherits=children[ind + 1] if ind != -1 else constants.types.OBJECT,
            line=line,
            sem_kind=constants.CLASS,
            param_method=constants.REF            
        )
        
        self.symbol_table.insert(table_item)
    
    def insert_feature(self, ctx: YaplParser.FeatureContext):
        children, line = self.get_ctx_attr(ctx)
        ind = indx(children, constants.TYPE_DELIMITER)
        sem_kind = constants.METHOD if children[1] != constants.TYPE_DELIMITER else constants.ATTR    
        
        table_item = TableItem(
            lex=children[0],
            token=ctx.children[1].symbol.type,
            typ=children[ind + 1],
            line=line,
            sem_kind=sem_kind,
            param_method=constants.REF
        )
        self.symbol_table.insert(table_item)
        
        if sem_kind == constants.METHOD:
            self.symbol_table.push_scope(children[0])
        

        
    def insert_formal(self, ctx: YaplParser.FormalContext):
        children, line = self.get_ctx_attr(ctx)
        
        table_item = TableItem(
            lex=children[0],
            token=ctx.children[1].symbol.type,
            typ=children[2],
            line=line,
            sem_kind=constants.PARAMETER,
            param_method=constants.REF,
        )
        
        self.symbol_table.insert(table_item)
        
    def insert_expr(self, ctx: YaplParser.ExprContext):
        pass
    
    def push_scope(self, name):
        self.symbol_table.push_scope(name)
        
    def pop_scope(self):
        self.symbol_table.pop_scope()
        
    def check_main(self):
        return self.symbol_table.check_main()
    
    @property
    def table(self) -> SymbolTable:
        return self.symbol_table
    