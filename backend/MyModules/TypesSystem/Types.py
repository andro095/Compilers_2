import json

import TypesSystem
from .Constants import types_sys_constants, types, basic_types
from SymbolTable import SymbolTable

from YAPL import YaplParser
from Global import global_constants

class TypeSystem:
    def __init__(self):
        self.individual_types = {}
        self.complex_types = {}
        # self.read_individual_types()
        # self.read_complex_types()
        
        self.rules ={
            (types.ID, types.ASIGN): self.assign,
            (types_sys_constants.EXPR, types.ARROBA): 'EXPR ARROBA',
            (types_sys_constants.EXPR, types.POINT): 'EXPR POINT',
            (types.ID, types.LROUND): 'ID LROUND',
            (types.IF, types_sys_constants.EXPR): 'IF EXPR',
            (types.WHILE, types_sys_constants.EXPR): 'WHILE EXPR',
            (types.LCURLY, types_sys_constants.EXPR): 'LCURLY EXPR',
            (types.LET, types.ID): 'LET ID',
            (types.ISVOID, types_sys_constants.EXPR): self.is_void,
            (types_sys_constants.EXPR, types.ADD): self.arimetic,
            (types_sys_constants.EXPR, types.SUB): self.arimetic,
            (types_sys_constants.EXPR, types.MULTIPLY): self.arimetic,
            (types_sys_constants.EXPR, types.DIVIDE): self.arimetic,
            (types.INT_NOT, types_sys_constants.EXPR): self.not_int,
            (types_sys_constants.EXPR, types.LESS_THAN): self.compare,
            (types_sys_constants.EXPR, types.LESS_EQUAL): self.compare,
            (types_sys_constants.EXPR, types.EQUAL): self.compare,
            (types.NOT, types_sys_constants.EXPR): self.not_expr,
            (types.LROUND, types_sys_constants.EXPR): self.lround_expr,
            
        }
        self.sym_table = SymbolTable()
        
    def get_father(self, clas: str) -> str:
        table_item = self.sym_table.get(clas)
        return table_item.inherits if table_item.inherits is not None else clas
        

    def read_individual_types(self):
        with open(types_sys_constants.INDIVIDUAL_RULES, 'r') as f:
            self.individual_types = json.load(f)

    def read_complex_types(self):
        with open(types_sys_constants.COMPLEX_RULES, 'r') as f:
            self.complex_types = json.load(f)
            
    def get_base_case_type(self, ctx: YaplParser.ExprContext) -> str:              
        if ctx.children[0].symbol.type == types.NEW:
            return ctx.children[1].getText() if self.sym_table.exists(ctx.children[1].getText()) else global_constants.ERROR_TYPE
        elif ctx.getChildCount() == 1 and ctx.children[0].symbol.type == types.ID:
            if self.sym_table.exists(ctx.children[0].getText()):
                return self.sym_table.get(ctx.children[0].getText()).typ
            else:
                return global_constants.ERROR_TYPE
        elif ctx.children[0].symbol.type == types.INTEGER:
            return basic_types.INT
        elif ctx.children[0].symbol.type == types.STRING:
            return basic_types.STRING
        elif ctx.children[0].symbol.type == types.TRUE or ctx.children[0].symbol.type == types.FALSE:
            return basic_types.BOOL
    
    def get_key_tuple(self, ctx: YaplParser.ExprContext, res: list[bool]) -> tuple:
        elem0 = types_sys_constants.EXPR if not res[0] else ctx.children[0].symbol.type
        elem1 = types_sys_constants.EXPR if not res[1] else ctx.children[1].symbol.type
        return (elem0, elem1)
        
    def validate_expr(self, ctx: YaplParser.ExprContext, types: list[str] ,res: list[bool]) -> str:
        print(ctx.getText(), types, res)
        rule = self.rules[self.get_key_tuple(ctx, res)]
        if not isinstance(rule, str):
            return rule(ctx, types)
        return 'Me'
    
    def validate_formal(self, ctx: YaplParser.FormalContext) -> str:
        if self.sym_table.exists(ctx.children[0].getText()) and self.sym_table.exists(ctx.children[2].getText()):
            return ctx.children[2].getText()
        else:
            return global_constants.ERROR_TYPE
        
    def lround_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        return types[1]
    
    def is_void(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        return basic_types.BOOL if types[1] != global_constants.ERROR_TYPE else global_constants.ERROR_TYPE
    
    def compare(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:        
        if types[0] == global_constants.ERROR_TYPE or types[2] == global_constants.ERROR_TYPE:
            return global_constants.ERROR_TYPE
        
        if self.sym_table.exists(types[0]) and self.sym_table.exists(types[2]):
            if types[0] == types[2]:
                return basic_types.BOOL
            else:
                father0 = self.get_father(types[0])
                father2 = self.get_father(types[2])
                
                if father0 == father2:
                    return basic_types.BOOL
                else:
                    return global_constants.ERROR_TYPE
        else: 
            return global_constants.ERROR_TYPE
            
    def not_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        return basic_types.BOOL if types[1] == basic_types.BOOL else global_constants.ERROR_TYPE
    
    def arimetic(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        return basic_types.INT if types[0] == basic_types.INT and types[2] == basic_types.INT else global_constants.ERROR_TYPE
    
    def not_int(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        return basic_types.INT if types[1] == basic_types.INT else global_constants.ERROR_TYPE
    
    def assign(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if types[0] == global_constants.ERROR_TYPE or types[2] == global_constants.ERROR_TYPE:
            return global_constants.ERROR_TYPE
        
        if self.sym_table.exists(ctx.children[0].getText()) and self.sym_table.exists(types[2]):    
            if types[0] == types[2]:
                return types[2]
            else:
                father2 = self.get_father(types[2])
                
                if types[0] == father2:
                    return types[2]
                else:           
                    return global_constants.ERROR_TYPE
        else:
            return global_constants.ERROR_TYPE
        
        
            


types_sys = TypeSystem()
