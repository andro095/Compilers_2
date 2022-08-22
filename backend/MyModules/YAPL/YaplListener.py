# Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/Grammars/Inputs/YAPL/Yapl.g4 by ANTLR 4.10.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser

from SymbolTable import SymbolTable, TableOperations

from ConsoleMessages import MessagesDB

# TODO: Realizar la insersión de valores en las funciones exit
# This class defines a complete listener for a parse tree produced by YaplParser.
class YaplListener(ParseTreeListener):
    def __init__(self):
        self.table_operations = TableOperations(SymbolTable())
        self.msg_db = MessagesDB()
        self.logs = []
        
    def insert_scope_message(self):
        self.msg_db.insert_message('Scope actual: %s.' % self.table_operations.table.actual_scope, 'yellow')
    
    def insert_log(self, message: str, color: str = None):
        if color:
            self.msg_db.insert_message(message, color)
        else:
            self.msg_db.insert_message(message)

    # Enter a parse tree produced by YaplParser#program.
    def enterProgram(self, ctx: YaplParser.ProgramContext):
        self.insert_log('Entrando al programa.')
        self.insert_scope_message()

    # Exit a parse tree produced by YaplParser#program.
    def exitProgram(self, ctx: YaplParser.ProgramContext):
        self.insert_log('Saliendo del programa.')
        self.insert_scope_message()
        if not self.table_operations.check_main():
            # Todo: Cambiar el mensaje de error
            self.msg_db.insert_error((0, 0), 'No se encuentra la clase main o no esta declarada de manera correcta.')
        print('Tablas de símbolos:\n %s.' % str(self.table_operations.table))
        

    # Enter a parse tree produced by YaplParser#class.
    def enterClass(self, ctx: YaplParser.ClassContext):
        self.insert_log('Entrando a la clase %s.' % ctx.children[1].getText(), 'purple')
        self.table_operations.insert_class(ctx)
        self.table_operations.push_scope(ctx.children[1].getText())
        line = (ctx.children[0].symbol.line, ctx.children[0].symbol.column)
        self.table_operations.insert_self(line)
        self.insert_scope_message()

    # Exit a parse tree produced by YaplParser#class.
    def exitClass(self, ctx: YaplParser.ClassContext):
        self.insert_log('Saliendo de la clase %s.' % ctx.children[1].getText(), 'purple')
        self.table_operations.pop_scope()
        self.insert_scope_message()

    # Enter a parse tree produced by YaplParser#feature.
    def enterFeature(self, ctx: YaplParser.FeatureContext):
        self.insert_log('Entrando al atributo %s.' % ctx.children[0].getText(), 'blue')
        self.table_operations.insert_feature(ctx)

    # Exit a parse tree produced by YaplParser#feature.
    def exitFeature(self, ctx: YaplParser.FeatureContext):
        self.insert_log('Saliendo del atributo %s.' % ctx.children[0].getText(), 'blue')
        if ctx.children[1].getText() != ':':
            self.table_operations.pop_scope()
            self.insert_scope_message()

    # Enter a parse tree produced by YaplParser#formal.
    def enterFormal(self, ctx: YaplParser.FormalContext):
        self.insert_log('Entrando al parámetro %s.' % ctx.children[0].getText(), 'cyan')
        self.table_operations.insert_formal(ctx)

    # Exit a parse tree produced by YaplParser#formal.
    def exitFormal(self, ctx: YaplParser.FormalContext):
        self.insert_log('Saliendo del parámetro %s.' % ctx.children[0].getText(), 'cyan')

    # Enter a parse tree produced by YaplParser#expr.
    def enterExpr(self, ctx: YaplParser.ExprContext):
        if not ctx.children:
            return
        self.insert_log('Entrando a la expresión %s.' % ctx.getText(), 'red')
        self.insert_scope_message()

    # Exit a parse tree produced by YaplParser#expr.
    def exitExpr(self, ctx: YaplParser.ExprContext):
        self.insert_log('Saliendo de la expresión %s.' % ctx.getText(), 'red')
        self.insert_scope_message()


del YaplParser
