from antlr4 import ParseTreeVisitor
from antlr4.tree.Tree import TerminalNodeImpl

if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser
    
from ConsoleMessages import MessagesDB

from .YaplUtils import evaluate_terminal_children, some_error_type
from Global import global_constants

from SymbolTable import SymbolTable, TableItem
from TypesSystem import types_sys


    
    
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
    
    # Visit a parse tree produced by YaplParser#program.
    def visitProgram(self, ctx:YaplParser.ProgramContext):
        res = evaluate_terminal_children(ctx.children)
        
        typs = self.visit_children(ctx, res)
        
        if some_error_type(typs):
            return global_constants.results_types.ERROR_TYPE
            
        return global_constants.results_types.CHECK_TYPE
        
    
    # Visit a parse tree produced by YaplParser#class.
    def visitClass(self, ctx:YaplParser.ClassContext):
        
        res = evaluate_terminal_children(ctx.children)  
        
        class_exists = self.symbol_table.exists(ctx.children[1].getText())
        
        if class_exists:
            self.symbol_table.enter_scope(ctx.children[1].getText())
            typs = self.visit_children(ctx, res)
            
            
            if some_error_type(typs):
                return global_constants.results_types.ERROR_TYPE
            
            self.symbol_table.exit_scope()
            
            return global_constants.results_types.CHECK_TYPE
        else:
            return global_constants.results_types.ERROR_TYPE
        
    
    # Visit a parse tree produced by YaplParser#feature.
    def visitFeature(self, ctx:YaplParser.FeatureContext):

        res = evaluate_terminal_children(ctx.children)
        
        feature_exists = self.symbol_table.exists(ctx.children[0].getText())
        
        typs = []
        
        if feature_exists:
            feature: TableItem = self.symbol_table.get(ctx.children[0].getText())
            
            if feature.sem_kind == global_constants.sem_kinds.METHOD:
                self.symbol_table.enter_scope(ctx.children[0].getText())
                
            typs = self.visit_children(ctx, res)
            
            
            if some_error_type(typs):
                return global_constants.results_types.ERROR_TYPE
            
            validation = types_sys.validate_feature(ctx, typs)
            
            if feature.sem_kind == global_constants.sem_kinds.METHOD:
                self.symbol_table.exit_scope()
                
            return validation
        else:
            return global_constants.results_types.ERROR_TYPE
        

    # Visit a parse tree produced by YaplParser#formal.
    def visitFormal(self, ctx:YaplParser.FormalContext):
        
        return types_sys.validate_formal(ctx)
    
    # Visit a parse tree produced by YaplParser#expr.
    def visitExpr(self, ctx:YaplParser.ExprContext):
        
        if not ctx.children:
            return global_constants.results_types.ERROR_TYPE
        
        res = evaluate_terminal_children(ctx.children) 
                
        typs = []
        
        if all(res) and len(ctx.children) < 3:
            typs = self.get_type(ctx)
            
            ctx.r_type = typs
            
            return typs
        else:
            if ctx.children[0].getText().lower() == global_constants.string_cons.LET:
                let_exists = self.symbol_table.exists(global_constants.string_cons.LET + str(self.analized_lets))
                if let_exists:
                    self.symbol_table.enter_scope(global_constants.string_cons.LET + str(self.analized_lets))
                else:
                    line = (ctx.start.line, ctx.start.column)
                    self.msg_db.insert_error(line, f'La let no existe.')
                    return global_constants.results_types.ERROR_TYPE
                
            typs = self.visit_children(ctx, res)
            
            if some_error_type(typs):
                return global_constants.results_types.ERROR_TYPE
        
            validation = types_sys.validate_expr(ctx, typs, res)
            
            if ctx.children[0].getText().lower() == global_constants.string_cons.LET:
                self.symbol_table.exit_scope()
                self.analized_lets += 1
                
            ctx.r_type = validation
            return validation


del YaplParser

