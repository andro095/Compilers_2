# Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/Grammars/Inputs/YAPL/Yapl.g4 by ANTLR 4.10.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser

from SymbolTable import SymbolTable, TableOperations

from ConsoleMessages import MessagesDB

from .YaplConstants import constants

# TODO: Realizar la insersión de valores en las funciones exit
# This class defines a complete listener for a parse tree produced by YaplParser.
class YaplListener(ParseTreeListener):

    # Enter a parse tree produced by YaplParser#program.
    def enterProgram(self, ctx: YaplParser.ProgramContext):
        pass

    # Exit a parse tree produced by YaplParser#program.
    def exitProgram(self, ctx: YaplParser.ProgramContext):
        pass
        

    # Enter a parse tree produced by YaplParser#class.
    def enterClass(self, ctx: YaplParser.ClassContext):
        pass

    # Exit a parse tree produced by YaplParser#class.
    def exitClass(self, ctx: YaplParser.ClassContext):
        pass

    # Enter a parse tree produced by YaplParser#feature.
    def enterFeature(self, ctx: YaplParser.FeatureContext):
        pass

    # Exit a parse tree produced by YaplParser#feature.
    def exitFeature(self, ctx: YaplParser.FeatureContext):
        pass

    # Enter a parse tree produced by YaplParser#formal.
    def enterFormal(self, ctx: YaplParser.FormalContext):
        pass

    # Exit a parse tree produced by YaplParser#formal.
    def exitFormal(self, ctx: YaplParser.FormalContext):
        pass

    # Enter a parse tree produced by YaplParser#expr.
    def enterExpr(self, ctx: YaplParser.ExprContext):
        pass

    # Exit a parse tree produced by YaplParser#expr.
    def exitExpr(self, ctx: YaplParser.ExprContext):
        pass


del YaplParser
