from calendar import c
from antlr4 import ParseTreeVisitor

if __name__ is not None and "." in __name__:
    from .YaplParser import YaplParser
else:
    from YaplParser import YaplParser
    
from SymbolTable import SymbolTable, MemoryDescriptor
from ConsoleMessages import MessagesDB
from .YaplUtils import evaluate_terminal_children
from InterCode import InterCodeItem, InterCode

from Global import global_constants


class YaplInterCodeVisitor(ParseTreeVisitor):
    
    def __init__(self) -> None:
        self.symbol_table = SymbolTable()
        self.msg_db = MessagesDB()
        self.intercode = InterCode()
        self.analized_lets = 0
        
        
    
    def get_base_type(self, ctx: YaplParser.ExprContext) -> InterCodeItem:
        return self.intercode.get_base_type(ctx)
        
    def visit_children(self, ctx, res: list[bool]) -> list[InterCodeItem]:
        inter_code = []
        for i, child in enumerate(ctx.children):
            if not res[i]:
                inter_code.append(child.accept(self))
            else:
                inter_code.append(None)
        return inter_code
        
    
    def visitProgram(self, ctx:YaplParser.ProgramContext):
        res = evaluate_terminal_children(ctx.children)
        
        # print(f'Scope actual: {self.symbol_table.actual_scope_name}')
        
        self.intercode.add_quadruple(op='goto', arg1='mainMain')
        
        intercodes = self.visit_children(ctx, res)
        
        intercodes = list(filter(lambda x: x is not None, intercodes))
        
        inter_code_item = self.intercode.evaluate_program(ctx, intercodes)
        
        # print(MemoryDescriptor())
        
        
        self.intercode.print_quadruple()
        return inter_code_item.code  
        
    def visitClass(self, ctx:YaplParser.ClassContext):
        res = evaluate_terminal_children(ctx.children)
                
        self.symbol_table.enter_scope(ctx.children[1].getText())
        
        self.intercode.add_quadruple(op='class_sepator', arg1=ctx.children[1].getText())
        
        self.intercode.increase_tabs()
        
        intercodes = self.visit_children(ctx, res)
        intercodes = list(filter(lambda x: x is not None, intercodes))
        
        
        self.symbol_table.exit_scope()
        
        intercode_item = self.intercode.evaluate_class(ctx, intercodes)
        self.intercode.decrease_tabs()        
        return intercode_item
        
    
    def visitFeature(self, ctx:YaplParser.FeatureContext):
        res = evaluate_terminal_children(ctx.children)
        
        feature = self.symbol_table.get(ctx.children[0].getText())
        
        intercodes = None
        
        
        
        if feature.sem_kind == global_constants.sem_kinds.METHOD:
            self.intercode.add_quadruple(op='label', arg1=f'{self.symbol_table.actual_scope_name.lower()}{feature.lex.capitalize()}')
            
            self.symbol_table.enter_scope(ctx.children[0].getText())
            
            
            
            self.intercode.increase_tabs()
            
            intercodes = self.visit_children(ctx, res)
            
            self.symbol_table.exit_scope()
        else:
            if len(ctx.children) > 3:
                intercodes = self.visit_children(ctx, res)
                
        if intercodes is None:
            return None
        
        intercodes = list(filter(lambda x: x is not None, intercodes))     
        inter_code_item = self.intercode.evaluate_feature(ctx, intercodes)
        
        if feature.sem_kind == global_constants.sem_kinds.METHOD:
            self.intercode.decrease_tabs()
            
        
        return inter_code_item
    
    def visitFormal(self, ctx:YaplParser.FormalContext):
        return None
        
    def visitExpr(self, ctx:YaplParser.ExprContext):
        res = evaluate_terminal_children(ctx.children)
        
        if all(res) and len(ctx.children) < 3:
            return self.get_base_type(ctx)
        else:            
            if res[0] and ctx.children[0].symbol.type == global_constants.token_types.LET:
                self.symbol_table.enter_scope(f'let{self.analized_lets}')
            
            if res[0] and ctx.children[0].symbol.type in global_constants.COND_TOKENS:
                self.intercode.increase_tabs()
            
            intercodes = self.visit_children(ctx, res)
            intercodes = list(filter(lambda x: x is not None, intercodes))

            if res[0] and ctx.children[0].symbol.type in global_constants.COND_TOKENS:
                self.intercode.decrease_tabs()
                
            if res[0] and ctx.children[0].symbol.type == global_constants.token_types.LET:
                self.symbol_table.exit_scope()
                self.analized_lets += 1
            
            return self.intercode.evaluate_expr(ctx, intercodes, res)