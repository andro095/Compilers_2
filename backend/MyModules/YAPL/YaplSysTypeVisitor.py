from antlr4 import *

if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser
    
from ConsoleMessages import MessagesDB
    
    
class YaplSysTypeVisitor(ParseTreeVisitor):
    
    def __init__(self) -> None:
    
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
    
    # Visit a parse tree produced by YaplParser#class.
    def visitClass(self, ctx:YaplParser.ClassContext):
        self.insert_log('Entrando a la clase %s.' % ctx.children[1].getText(), 'purple')
        self.visitChildren(ctx)
        self.insert_log('Saliendo de la clase %s.' % ctx.children[1].getText(), 'purple')
        
    
    # Visit a parse tree produced by YaplParser#feature.
    def visitFeature(self, ctx:YaplParser.FeatureContext):
        self.insert_log('Entrando a la característica %s.' % ctx.children[0].getText(), 'blue')
        self.visitChildren(ctx)
        self.insert_log('Saliendo de la característica %s.' % ctx.children[0].getText(), 'blue')
        

    # Visit a parse tree produced by YaplParser#formal.
    def visitFormal(self, ctx:YaplParser.FormalContext):
        self.insert_log('Entrando al parámetro %s.' % ctx.children[0].getText(), 'green')
        self.visitChildren(ctx)
        self.insert_log('Saliendo del parámetro %s.' % ctx.children[0].getText(), 'green')

    
    # Visit a parse tree produced by YaplParser#expr.
    def visitExpr(self, ctx:YaplParser.ExprContext):
        has_children = ctx.getChildCount() > 0
        children = list(ctx.getChildren())
        self.insert_log(f'Entrando a la expresión {ctx.getText()} y el estado de su children es {has_children} y su children es {children}.', 'pink')
        self.visitChildren(ctx)
        self.insert_log(f'Saliendo de la expresión {ctx.getText()} y el estado de su children es {has_children} y su children es {children}.', 'pink')


del YaplParser

