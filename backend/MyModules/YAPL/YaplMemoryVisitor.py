from antlr4 import ParseTreeVisitor
if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser
    
from SymbolTable import SymbolTable, TableOperations
from ConsoleMessages import MessagesDB

from Global import global_constants

class YaplMemoryVisitor(ParseTreeVisitor):
    
    def __init__(self) -> None:
        self.symbol_table = SymbolTable()
        self.table_operations = TableOperations()
        self.msg_db = MessagesDB()
        
    def increase_memory_pos(self, byte_size: int, mem_base: int) -> int:
        if mem_base == global_constants.base_memory.HEAP:
            return self.symbol_table.increase_heap_pos(byte_size)
        else:
            return self.symbol_table.increase_stack_pos(byte_size)
    
    def visitProgram(self, ctx:YaplParser.ProgramContext):
        print('Programa')
        self.visitChildren(ctx)
        print('Tablas de símbolos:\n %s.' % str(self.symbol_table))
        
    def visitClass(self, ctx:YaplParser.ClassContext):
        self.symbol_table.enter_scope(ctx.children[1].getText())
        self.visitChildren(ctx)
        self.symbol_table.exit_scope()
    
    def visitFeature(self, ctx:YaplParser.FeatureContext):
        table_item = self.symbol_table.get(ctx.children[0].getText())
        mem_pos = self.increase_memory_pos(table_item.byte_size, table_item.mem_base)
        self.symbol_table.set_mem_pos(table_item.lex, mem_pos)
        if table_item.sem_kind == global_constants.sem_kinds.METHOD:
            self.symbol_table.enter_scope(ctx.children[0].getText())
            self.visitChildren(ctx)
            self.symbol_table.exit_scope()
    
    def visitFormal(self, ctx:YaplParser.FormalContext):
        table_item = self.symbol_table.get(ctx.children[0].getText())
        mem_pos = self.increase_memory_pos(table_item.byte_size, table_item.mem_base)
        self.symbol_table.set_mem_pos(table_item.lex, mem_pos)
        
    def visitExpr(self, ctx:YaplParser.ExprContext):
        print('Expr')
        self.visitChildren(ctx)