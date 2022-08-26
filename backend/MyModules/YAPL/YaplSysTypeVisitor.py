from ast import Param
from asyncio import constants
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl

if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser
    
from ConsoleMessages import MessagesDB

from .YaplUtils import evaluate_terminal_children, get_no_terminal_indexes, some_error_type
from Global import global_constants

from SymbolTable import SymbolTable, TableItem
from TypesSystem import types_sys

from .YaplConstants import constants
    
    
class YaplSysTypeVisitor(ParseTreeVisitor):
    
    def __init__(self) -> None:
        self.msg_db = MessagesDB()
        self.symbol_table = SymbolTable()
        self.analized_lets = 0
        
    def get_type(self, child: YaplParser.ExprContext) -> str:
        return types_sys.get_base_case_type(child)
        
    def visit_children(self, ctx, res: list[bool]) -> list[str]:
        res_types = []
        for i, child in enumerate(ctx.children):
            if not res[i]:
                res_types.append(child.accept(self))
            else:
                res_types.append(None)
        return res_types
        
    def insert_log(self, message: str, color: str = None):
        if color:
            self.msg_db.insert_message(message, color)
        else:
            self.msg_db.insert_message(message)
    
    # Visit a parse tree produced by YaplParser#program.
    def visitProgram(self, ctx:YaplParser.ProgramContext):
        print(self.symbol_table.actual_scope)
        
        res = evaluate_terminal_children(ctx.children)
        
        typs = self.visit_children(ctx, res)
        # self.msg_db.insert_message("Programa: " + str(typs))
        
        if some_error_type(typs):
                line = (ctx.start.line, ctx.start.column)
                self.msg_db.insert_error(line, f'No se puede iniciar el programa porque hay errores aqui:\n\t\t{ctx.getText()}')
                return global_constants.ERROR_TYPE
            
        return global_constants.CHECK_TYPE
        
    
    # Visit a parse tree produced by YaplParser#class.
    def visitClass(self, ctx:YaplParser.ClassContext): 
        if self.msg_db.error_flag:
            return global_constants.ERROR_TYPE
        
        res = evaluate_terminal_children(ctx.children)  
        
        class_exists = self.symbol_table.exists(ctx.children[1].getText())
        
        if class_exists:
            self.symbol_table.enter_scope(ctx.children[1].getText())
            typs = self.visit_children(ctx, res)
            # self.msg_db.insert_message(f"Clase {ctx.children[1].getText()}: " + str(typs))
            
            if some_error_type(typs):
                line = (ctx.start.line, ctx.start.column)
                self.msg_db.insert_error(line, f'No se puede iniciar el programa porque hay errores aqui:\n\t\t{ctx.getText()}')
                return global_constants.ERROR_TYPE
            
            self.symbol_table.exit_scope()
            
            return global_constants.CHECK_TYPE
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msg_db.insert_error(line, f'La clase {ctx.children[1].getText()} no existe.')
            return global_constants.ERROR_TYPE
        
    
    # Visit a parse tree produced by YaplParser#feature.
    def visitFeature(self, ctx:YaplParser.FeatureContext):
        if self.msg_db.error_flag:
            return global_constants.ERROR_TYPE

        res = evaluate_terminal_children(ctx.children)
        
        feature_exists = self.symbol_table.exists(ctx.children[0].getText())
        
        typs = []
        
        if feature_exists:
            feature: TableItem = self.symbol_table.get(ctx.children[0].getText())
            
            if feature.sem_kind == global_constants.METHOD:
                self.symbol_table.enter_scope(ctx.children[0].getText())
                
            typs = self.visit_children(ctx, res)
            # self.msg_db.insert_message(f"Feature {ctx.children[0].getText()}: " + str(typs))
            
            if some_error_type(typs):
                line = (ctx.start.line, ctx.start.column)
                self.msg_db.insert_error(line, f'No se puede iniciar el programa porque hay errores aqui:\n\t\t{ctx.getText()}')
                return global_constants.ERROR_TYPE
            
            validation = types_sys.validate_feature(ctx, typs)
            
            if feature.sem_kind == global_constants.METHOD:
                self.symbol_table.exit_scope()
                
            return validation
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msg_db.insert_error(line, f'El atributo {ctx.children[0].getText()} no existe.')
            return global_constants.ERROR_TYPE
        

    # Visit a parse tree produced by YaplParser#formal.
    def visitFormal(self, ctx:YaplParser.FormalContext):
        if self.msg_db.error_flag:
            return global_constants.ERROR_TYPE
        
        # res = evaluate_terminal_children(ctx.children)     
        
        # self.msg_db.insert_message(f"Formal {ctx.children[0].getText()}: " + str(res))
        
        return types_sys.validate_formal(ctx)
    
    # Visit a parse tree produced by YaplParser#expr.
    def visitExpr(self, ctx:YaplParser.ExprContext):  
        if self.msg_db.error_flag:
            return global_constants.ERROR_TYPE
        
        res = evaluate_terminal_children(ctx.children) 
                
        typs = []
        
        if all(res):
            typs = self.get_type(ctx)
            # self.msg_db.insert_message(f"Expr {ctx.getText()}: " + str(typs))
            return typs
        else:
            if ctx.children[0].getText().lower() == constants.LET:
                let_exists = self.symbol_table.exists(constants.LET + str(self.analized_lets))
                if let_exists:
                    self.symbol_table.enter_scope(constants.LET + str(self.analized_lets))
                else:
                    line = (ctx.start.line, ctx.start.column)
                    self.msg_db.insert_error(line, f'La let no existe.')
                    return global_constants.ERROR_TYPE
                
            typs = self.visit_children(ctx, res)
            # self.msg_db.insert_message(f"Expr {ctx.getText()}: " + str(typs))
            
            if some_error_type(typs):
                line = (ctx.start.line, ctx.start.column)
                self.msg_db.insert_error(line, f'No se puede iniciar el programa porque hay errores aqui:\n\t\t{ctx.getText()}')
                return global_constants.ERROR_TYPE
        
            validation = types_sys.validate_expr(ctx, typs, res)
            
            if ctx.children[0].getText().lower() == constants.LET:
                self.symbol_table.exit_scope()
                self.analized_lets += 1
                
            return validation


del YaplParser

