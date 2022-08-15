from .Table import SymbolTable
from .Constants import constants
from YAPL import YaplParser
from utils import indx

class TableOperations:
    def __init__(self, symbol_table: SymbolTable) -> None:
        self.symbol_table: SymbolTable = symbol_table
        
    def assign_value(self, ctx: YaplParser.ExprContext):
        self.symbol_table.set(ctx.children[0].getText(), ctx.children[0].symbol.line, ctx.children[2].getText())
    
    def insert_self(self, line: int):
        name = 'self'
        kind = constants.ATTR
        typ = constants.SELF_TYPE
        scope = self.symbol_table.get_scope()
        self.symbol_table.insert(name, typ, kind, scope, line)
        
    def insert_class(self, ctx: YaplParser.ClassContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[1]
        kind = constants.CLASS
        ind = indx(children, 'inherits')
        typ = children[ind + 1] if ind != -1 else 'Object'
        line = ctx.children[0].symbol.line
        scope = self.symbol_table.get_scope()
        self.symbol_table.insert(name, typ, kind, scope, line)
    
    def insert_feature(self, ctx: YaplParser.FeatureContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        kind = constants.METHOD if children[1] != ':' else constants.ATTR
        ind = indx(children, ':')
        typ = children[ind + 1]
        line = ctx.children[0].symbol.line
        value = None
        scope = self.symbol_table.get_scope()

        if kind == 'method':
            self.symbol_table.push_scope(children[0])
        else:
            index = indx(children, '<-')
            if index != -1:
                value = children[index + 1]

        self.symbol_table.insert(name, typ, kind, scope, line, value)
        
    def insert_formal(self, ctx: YaplParser.FormalContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        kind = constants.PARAMETER
        typ = children[2]
        line = ctx.children[0].symbol.line
        scope = self.symbol_table.get_scope()
        self.symbol_table.insert(name, typ, kind, scope, line)
        
    def insert_expr(self, ctx: YaplParser.ExprContext):
        pass
    
    def push_scope(self, name):
        self.symbol_table.push_scope(name)
        
    def pop_scope(self):
        self.symbol_table.pop_scope()
    
    def get_table(self) -> SymbolTable:
        return self.symbol_table
    