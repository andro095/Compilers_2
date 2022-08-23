# Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/Grammars/Inputs/YAPL/Yapl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser
    
from SymbolTable import SymbolTable, TableOperations

from ConsoleMessages import MessagesDB

from .YaplConstants import constants

# This class defines a complete generic visitor for a parse tree produced by YaplParser.

class YaplVisitor(ParseTreeVisitor):
    
    def __init__(self) -> None:
        self.symbol_table = SymbolTable()
        self.table_operations = TableOperations()
        self.msg_db = MessagesDB()
        
    def insert_log(self, message: str, color: str = None):
        if color:
            self.msg_db.insert_message(message, color)
        else:
            self.msg_db.insert_message(message)


    # Visit a parse tree produced by YaplParser#program.
    def visitProgram(self, ctx:YaplParser.ProgramContext):
        self.insert_log('Entrando al programa.')
        self.visitChildren(ctx)
        self.insert_log('Saliendo del programa.')
        self.symbol_table.check_main()
        print('Tablas de símbolos:\n %s.' % str(self.symbol_table))


    # Visit a parse tree produced by YaplParser#class.
    def visitClass(self, ctx:YaplParser.ClassContext):
        self.insert_log('Entrando a la clase %s.' % ctx.children[1].getText(), 'purple')
        inserted = self.table_operations.insert_class(ctx)
        if inserted:
            self.symbol_table.push_scope(ctx.children[1].getText())
            line = (ctx.children[0].symbol.line, ctx.children[0].symbol.column)
            self.table_operations.insert_self(line)
            self.visitChildren(ctx)
            self.symbol_table.pop_scope()
            
        self.insert_log('Saliendo de la clase %s.' % ctx.children[1].getText(), 'purple')
        # pass


    # Visit a parse tree produced by YaplParser#feature.
    def visitFeature(self, ctx:YaplParser.FeatureContext):
        self.insert_log('Entrando a la característica %s.' % ctx.children[0].getText(), 'blue')
        inserted = self.table_operations.insert_feature(ctx)
        if inserted:
            if ctx.children[1].getText() != constants.TYPE_DELIMITER:
                self.symbol_table.push_scope(ctx.children[0].getText()) 
                
            self.visitChildren(ctx)
            
            if ctx.children[1].getText() != constants.TYPE_DELIMITER:
                self.symbol_table.pop_scope()
        self.insert_log('Saliendo de la característica %s.' % ctx.children[0].getText(), 'blue')


    # Visit a parse tree produced by YaplParser#formal.
    def visitFormal(self, ctx:YaplParser.FormalContext):
        self.insert_log('Entrando al parámetro %s.' % ctx.children[0].getText(), 'green')
        self.table_operations.insert_formal(ctx)
        self.insert_log('Saliendo del parámetro %s.' % ctx.children[0].getText(), 'green')


    # Visit a parse tree produced by YaplParser#expr.
    def visitExpr(self, ctx:YaplParser.ExprContext):
        self.insert_log('Entrando a la expresión %s.' % ctx.getText(), 'pink')
        if not ctx.children:
            return
        if ctx.children[0].getText().lower() == constants.LET:
            inserted = self.table_operations.insert_expr(ctx)
            if inserted:
                self.visitChildren(ctx)
                
        self.insert_log('Entrando a la expresión %s.' % ctx.getText(), 'pink')



del YaplParser