# Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/backend/MyModules/YAPL/Yapl.g4 by ANTLR 4.10.1
from antlr4 import ParseTreeVisitor
if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser
    
from SymbolTable import SymbolTable, TableOperations
from ConsoleMessages import MessagesDB

from Global import global_constants

# This class defines a complete generic visitor for a parse tree produced by YaplParser.

class YaplVisitor(ParseTreeVisitor):
    
    def __init__(self) -> None:
        self.symbol_table = SymbolTable()
        self.table_operations = TableOperations()
        self.msg_db = MessagesDB()
        
    def get_class_total_size(self, name: str) -> int:
        for symbol in self.symbol_table.tables[0].items:
            if symbol.lex == name:
                return symbol.byte_size

    # Visit a parse tree produced by YaplParser#program.
    def visitProgram(self, ctx:YaplParser.ProgramContext):
        self.visitChildren(ctx)
        self.symbol_table.check_main()
        print('Tablas de símbolos:\n %s.' % str(self.symbol_table))


    # Visit a parse tree produced by YaplParser#class.
    def visitClass(self, ctx:YaplParser.ClassContext):
        inserted = self.table_operations.insert_class(ctx)
        if inserted:
            self.symbol_table.push_scope(ctx.children[1].getText())
            line = (ctx.children[0].symbol.line, ctx.children[0].symbol.column)
            self.table_operations.insert_self(line)
            self.visitChildren(ctx)
            print(f'{ctx.children[1].getText()}, {self.symbol_table.tables[self.symbol_table.actual_scope].name}')
            actual_table = self.symbol_table.tables[self.symbol_table.actual_scope]
            byte_sizes = list(map(lambda symbol: symbol.byte_size if symbol.typ != actual_table.name else 0, actual_table.items))
            self.symbol_table.add_byte_size(0, actual_table.name, sum(byte_sizes))
            byte_size = self.get_class_total_size(actual_table.name)
            
            for item in self.symbol_table.tables[self.symbol_table.actual_scope].items:
                if item.typ == actual_table.name:
                    item.byte_size = byte_size
            self.symbol_table.pop_scope()


    # Visit a parse tree produced by YaplParser#feature.
    def visitFeature(self, ctx:YaplParser.FeatureContext):
        inserted = self.table_operations.insert_feature(ctx)
        if inserted:
            if ctx.children[1].getText() != global_constants.string_cons.TYPE_DELIMITER:
                self.symbol_table.push_scope(ctx.children[0].getText()) 
                
            self.visitChildren(ctx)
            
            if ctx.children[1].getText() != global_constants.string_cons.TYPE_DELIMITER:
                self.symbol_table.pop_scope()


    # Visit a parse tree produced by YaplParser#formal.
    def visitFormal(self, ctx:YaplParser.FormalContext):
        self.table_operations.insert_formal(ctx)


    # Visit a parse tree produced by YaplParser#expr.
    def visitExpr(self, ctx:YaplParser.ExprContext):
        if not ctx.children:
            return
        if ctx.children[0].getText().lower() == global_constants.string_cons.LET:
            inserted = self.table_operations.insert_expr(ctx)
            if inserted:
                self.visitChildren(ctx)
                



del YaplParser