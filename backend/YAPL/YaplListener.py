# Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/Grammars/Inputs/YAPL/Yapl.g4 by ANTLR 4.10.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser

from SymbolTable import SymbolTable, constants
from TypesSystem import types_sys
from utils import indx


# TODO: Mover la insersión de valores a una clase aparte
# TODO: Realizar la insersión de valores en las funciones exit
# This class defines a complete listener for a parse tree produced by YaplParser.
class YaplListener(ParseTreeListener):
    def __init__(self):
        self.symbol_table = SymbolTable()


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
            # #print(Fore.YELLOW, 'Scope actual: ', self.symbol_table.get_scope())
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
        # #print(Fore.YELLOW, 'Scope actual: ', self.symbol_table.get_scope())
        self.symbol_table.insert(name, typ, kind, scope, line)

    def insert_expr(self, ctx: YaplParser.ExprContext):
        pass

    # Enter a parse tree produced by YaplParser#program.
    def enterProgram(self, ctx: YaplParser.ProgramContext):
        pass
        # print(Fore.RESET, 'Programa hola: %s' % ctx.getText())
        # #print(Fore.YELLOW, 'Scope actual: ', self.symbol_table.get_scope())

    # Exit a parse tree produced by YaplParser#program.
    def exitProgram(self, ctx: YaplParser.ProgramContext):
        # print(Fore.RESET, 'Programa adios: %s' % ctx.getText())
        # #print(Fore.YELLOW, 'Scope actual: ', self.symbol_table.get_scope())
        print(str(self.symbol_table))
        return 'Programa adios: %s' % ctx.getText()

    # Enter a parse tree produced by YaplParser#class.
    def enterClass(self, ctx: YaplParser.ClassContext):
        # print(Fore.MAGENTA, 'Class: %s' % ctx.getText())
        self.insert_class(ctx)
        self.symbol_table.push_scope(ctx.children[1].getText())
        self.insert_self(ctx.children[0].symbol.line)
        # print(Fore.YELLOW, 'Scope actual: ', self.symbol_table.get_scope())

    # Exit a parse tree produced by YaplParser#class.
    def exitClass(self, ctx: YaplParser.ClassContext):
        # print(Fore.MAGENTA, 'Class adios : %s' % ctx.getText())
        self.symbol_table.pop_scope()
        # #print(Fore.YELLOW, 'Scope actual: ', self.symbol_table.get_scope())

    # Enter a parse tree produced by YaplParser#feature.
    def enterFeature(self, ctx: YaplParser.FeatureContext):
        # print(Fore.BLUE, 'Feature: %s' % ctx.getText())
        self.insert_feature(ctx)
        # #print(Fore.RESET)

    # Exit a parse tree produced by YaplParser#feature.
    def exitFeature(self, ctx: YaplParser.FeatureContext):
        # print(Fore.BLUE, 'Feature adios: %s' % ctx.getText())
        if ctx.children[1].getText() != ':':
            self.symbol_table.pop_scope()
            # #print(Fore.YELLOW, 'Scope actual: ', self.symbol_table.get_scope())

    # Enter a parse tree produced by YaplParser#formal.
    def enterFormal(self, ctx: YaplParser.FormalContext):
        # print(Fore.CYAN, 'Formal: %s' % ctx.getText())
        self.insert_formal(ctx)

    # Exit a parse tree produced by YaplParser#formal.
    def exitFormal(self, ctx: YaplParser.FormalContext):
        pass
        # print(Fore.CYAN, 'Formal adios: %s' % ctx.getText())
        # #print(Fore.YELLOW, 'Scope actual: ', self.symbol_table.get_scope())

    # Enter a parse tree produced by YaplParser#expr.
    def enterExpr(self, ctx: YaplParser.ExprContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        # print(Fore.RED, 'Expr: %s' % ctx.getText())
        if '<-' in children:
            self.assign_value(ctx)
            # print(Fore.YELLOW, ctx.children[0].symbol.type)

        # #print(Fore.YELLOW, 'Scope actual: ', self.symbol_table.get_scope())

    # Exit a parse tree produced by YaplParser#expr.
    def exitExpr(self, ctx: YaplParser.ExprContext):
        pass
        # return
        # print(Fore.RED, 'Expr adios: %s' % ctx.getText())
        # #print(Fore.YELLOW, 'Scope actual: ', self.symbol_table.get_scope())


del YaplParser
