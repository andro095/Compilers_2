# Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/Grammars/Inputs/YAPL/Yapl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser
    
from SymbolTable import SymbolTable, TableOperations

from ConsoleMessages import MessagesDB

from .YaplConstants import constants

from Global import global_constants

# This class defines a complete generic visitor for a parse tree produced by YaplParser.

class YaplVisitor(ParseTreeVisitor):
    
    def __init__(self) -> None:
        self.symbol_table = SymbolTable()
        self.table_operations = TableOperations()
        self.msg_db = MessagesDB()

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
            self.symbol_table.pop_scope()

    # Visit a parse tree produced by YaplParser#feature.
    def visitFeature(self, ctx:YaplParser.FeatureContext):
        inserted = self.table_operations.insert_feature(ctx)
        if inserted:
            if ctx.children[1].getText() != constants.TYPE_DELIMITER:
                self.symbol_table.push_scope(ctx.children[0].getText()) 
                
            self.visitChildren(ctx)
            
            if ctx.children[1].getText() != constants.TYPE_DELIMITER:
                self.symbol_table.pop_scope()


    # Visit a parse tree produced by YaplParser#formal.
    def visitFormal(self, ctx:YaplParser.FormalContext):
        self.table_operations.insert_formal(ctx)


    # Visit a parse tree produced by YaplParser#expr.
    def visitExpr(self, ctx:YaplParser.ExprContext):
 
        if not ctx.children:
            return
        if ctx.children[0].getText().lower() == constants.LET:
            inserted = self.table_operations.insert_expr(ctx)
            if inserted:
                self.visitChildren(ctx)
                



del YaplParser