# Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/Grammars/Inputs/YAPL/Yapl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser

# This class defines a complete generic visitor for a parse tree produced by YaplParser.

class YaplVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YaplParser#program.
    def visitProgram(self, ctx:YaplParser.ProgramContext):
        print(f'Entrando al programa {ctx.getText()}')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YaplParser#class.
    def visitClass(self, ctx:YaplParser.ClassContext):
        print(f'Entrando a la clase {ctx.getText()}')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YaplParser#feature.
    def visitFeature(self, ctx:YaplParser.FeatureContext):
        print(f'Entrando el atributo o método {ctx.getText()}')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YaplParser#formal.
    def visitFormal(self, ctx:YaplParser.FormalContext):
        print(f'Entrando al parámetro {ctx.getText()}')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YaplParser#expr.
    def visitExpr(self, ctx:YaplParser.ExprContext):
        print(f'Entrando a la expresión {ctx.getText()}')
        return self.visitChildren(ctx)



del YaplParser