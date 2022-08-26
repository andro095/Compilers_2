import json
from SymbolTable.Table import TableItem

from ConsoleMessages import MessagesDB
from .Constants import types_sys_constants, typs, basic_types
from SymbolTable import SymbolTable

from YAPL import YaplParser
from Global import global_constants
from antlr4.tree.Tree import TerminalNodeImpl

def is_terminal_node(node) -> bool:
    return isinstance(node, TerminalNodeImpl)

class TypeSystem:
    def __init__(self):
        self.msgs_db = MessagesDB()
        
        self.rules ={
            (typs.ID, typs.ASIGN): self.assign,
            (types_sys_constants.EXPR, typs.ARROBA): self.expr_arroba,
            (types_sys_constants.EXPR, typs.POINT): self.expr_point,
            (typs.ID, typs.LROUND): self.id_lround,
            (typs.IF, types_sys_constants.EXPR): self.if_expr,
            (typs.WHILE, types_sys_constants.EXPR): self.while_expr,
            (typs.LCURLY, types_sys_constants.EXPR): self.block,
            (typs.LET, typs.ID): self.let_expr,
            (typs.ISVOID, types_sys_constants.EXPR): self.is_void,
            (types_sys_constants.EXPR, typs.ADD): self.arimetic,
            (types_sys_constants.EXPR, typs.SUB): self.arimetic,
            (types_sys_constants.EXPR, typs.MULTIPLY): self.arimetic,
            (types_sys_constants.EXPR, typs.DIVIDE): self.arimetic,
            (typs.INT_NOT, types_sys_constants.EXPR): self.not_int,
            (types_sys_constants.EXPR, typs.LESS_THAN): self.compare,
            (types_sys_constants.EXPR, typs.LESS_EQUAL): self.compare,
            (types_sys_constants.EXPR, typs.EQUAL): self.compare,
            (typs.NOT, types_sys_constants.EXPR): self.not_expr,
            (typs.LROUND, types_sys_constants.EXPR): self.lround_expr,
            
        }
        self.sym_table = SymbolTable()
        
    def get_father(self, clas: str) -> str:
        table_item = self.sym_table.get(clas)
        return table_item.inherits if table_item.inherits is not None else clas
    
    def cast_int(self, clas: str) -> str:
        return basic_types.INT if clas == basic_types.BOOL else clas
    
    def cast_bool(self, clas: str) -> str:
        return basic_types.BOOL if clas == basic_types.INT else clas
        
    def get_base_case_type(self, ctx: YaplParser.ExprContext) -> str:              
        if ctx.children[0].symbol.type == typs.NEW:
            return ctx.children[1].getText() if self.sym_table.exists(ctx.children[1].getText()) else global_constants.ERROR_TYPE
        elif ctx.children[0].symbol.type == typs.ID:
            if self.sym_table.exists(ctx.children[0].getText()):
                elem: TableItem = self.sym_table.get(ctx.children[0].getText())
                if elem.sem_kind == global_constants.ATTR or elem.sem_kind == global_constants.PARAMETER:
                    if ctx.getChildCount() == 1:
                        return elem.typ
                    elif ctx.children[1].symbol.type == typs.POINT or ctx.children[1].symbol.type == typs.ASIGN:
                        return elem.typ
                    else:
                        line = (ctx.start.line, ctx.start.column)
                        self.msgs_db.insert_errror(line, f'No se puede acceder a {ctx.children[1].getText()} de una variable')
                        return global_constants.ERROR_TYPE
                elif elem.sem_kind == global_constants.METHOD:
                    if ctx.getChildCount() > 1 and ctx.children[1].symbol.type == typs.LROUND:
                        return elem.typ
                    else: 
                        line = (ctx.start.line, ctx.start.column)
                        self.msgs_db.insert_error(line, f'No se puede acceder a {ctx.children[1].getText()} de un método')
                        return global_constants.ERROR_TYPE
            else:
                line = (ctx.start.line, ctx.start.column)
                self.msgs_db.insert_error(line, f'{ctx.children[0].getText()} no existe')
                return global_constants.ERROR_TYPE
        elif ctx.children[0].symbol.type == typs.INTEGER:
            return basic_types.INT
        elif ctx.children[0].symbol.type == typs.STRING:
            return basic_types.STRING
        elif ctx.children[0].symbol.type == typs.TRUE or ctx.children[0].symbol.type == typs.FALSE:
            return basic_types.BOOL
    
    def get_key_tuple(self, ctx: YaplParser.ExprContext, res: list[bool]) -> tuple:
        elem0 = types_sys_constants.EXPR if not res[0] else ctx.children[0].symbol.type
        elem1 = types_sys_constants.EXPR if not res[1] else ctx.children[1].symbol.type
        return (elem0, elem1)
    
    def validate_feature(self, ctx: YaplParser.FeatureContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.ERROR_TYPE, types)):
            return global_constants.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(ctx.children[0].getText()):
            feature_item = self.sym_table.get(ctx.children[0].getText())
            if feature_item.sem_kind == global_constants.ATTR:
                if not self.sym_table.exists(ctx.children[2].getText()):
                    self.msgs_db.insert_error(line, f'Tipo {ctx.children[2].getText()} no existente')
                    return global_constants.ERROR_TYPE
                
                if ctx.getChildCount() == 3:
                    return global_constants.CHECK_TYPE
                
                if types[4] != feature_item.typ and types[4] != basic_types.SELF_TYPE:
                    self.msgs_db.insert_error(line, f'Tipo {types[4]} no es compatible con {feature_item.typ}')
                    return global_constants.ERROR_TYPE
                else:
                    return global_constants.CHECK_TYPE
            elif feature_item.sem_kind == global_constants.METHOD:
                if ctx.children[-4].getText() != basic_types.SELF_TYPE and not self.sym_table.exists(ctx.children[-4].getText()):
                    self.msgs_db.insert_error(line, f'Tipo {ctx.children[-4].getText()} no existente')
                    return global_constants.ERROR_TYPE
                
                if types[-2] == None:
                    self.msgs_db.insert_error(line, f'Sin tipo')
                    return global_constants.ERROR_TYPE
                
                if types[-2] != feature_item.typ and types[-2] != global_constants.NO_TYPE:
                    self.msgs_db.insert_error(line, f'Tipo {types[-2]} no es compatible con {feature_item.typ}')
                    return global_constants.ERROR_TYPE
                else:
                    return global_constants.CHECK_TYPE
        else:
            self.msgs_db.insert_error(line, f'{ctx.children[0].getText()} no existe')
            return global_constants.ERROR_TYPE
        
    def validate_expr(self, ctx: YaplParser.ExprContext, types: list[str] ,res: list[bool]) -> str:
        return self.rules[self.get_key_tuple(ctx, res)](ctx, types)
    
    def validate_formal(self, ctx: YaplParser.FormalContext) -> str:
        if self.sym_table.exists(ctx.children[0].getText()) and self.sym_table.exists(ctx.children[2].getText()):
            return global_constants.CHECK_TYPE
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msgs_db.insert_error(line, f'Paraetro {ctx.children[0].getText()} y/o tipo {ctx.children[2].getText()} no delcarado')
            return global_constants.ERROR_TYPE
        
    def lround_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        return types[1]
    
    def is_void(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if types[1] != global_constants.ERROR_TYPE:
            return basic_types.BOOL
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msgs_db.insert_error(line, f'{ctx.children[1].getText()} no es compatible con {types[1]}')
            return global_constants.ERROR_TYPE
    
    def compare(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:        
        if types[0] == global_constants.ERROR_TYPE or types[2] == global_constants.ERROR_TYPE:
            return global_constants.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(types[0]) and self.sym_table.exists(types[2]):
            if types[0] == types[2]:
                return basic_types.BOOL
            else:
                father0 = self.get_father(types[0])
                father2 = self.get_father(types[2])
                
                if father0 == father2 or types[0] == father2 or types[2] == father0:
                    return basic_types.BOOL
                else:
                    self.msgs_db.insert_error(line, f'{types[0]} no es compatible con {types[2]}')
                    return global_constants.ERROR_TYPE
        else: 
            self.msgs_db.insert_error(line, f'{types[0]} o {types[2]} no existe')
            return global_constants.ERROR_TYPE
            
    def not_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if self.cast_bool(types[1]) == basic_types.BOOL:
            return basic_types.BOOL
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msgs_db.insert_error(line, f'{types[1]} no es compatible con {basic_types.BOOL}')
            return global_constants.ERROR_TYPE
    
    def arimetic(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if self.cast_int(types[0]) == basic_types.INT and self.cast_int(types[2]) == basic_types.INT:
            return basic_types.INT
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msgs_db.insert_error(line, f'{types[0]} o {types[2]} no son enteros')
            return global_constants.ERROR_TYPE
    
    def not_int(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if self.cast_int(types[1]) == basic_types.INT:
            return basic_types.INT
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msgs_db.insert_error(line, f'{types[1]} no es compatible con {basic_types.INT}')
            return global_constants.ERROR_TYPE
            
    
    def assign(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if types[0] == global_constants.ERROR_TYPE or types[2] == global_constants.ERROR_TYPE:
            return global_constants.ERROR_TYPE
    
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(ctx.children[0].getText()) and self.sym_table.exists(types[2]):    
            id_item: TableItem = self.sym_table.get(ctx.children[0].getText())
            
            if id_item.typ == types[2]:
                return types[2]
            else:
                father2 = self.get_father(types[2])
                
                if id_item.typ == father2:
                    return types[2]
                else:           
                    self.msgs_db.insert_error(line, f'{id_item.typ} no es compatible con {types[2]}')
                    return global_constants.ERROR_TYPE
        else:
            self.msgs_db.insert_error(line, f'{ctx.children[0].getText()} o {types[2]} no existe')
            return global_constants.ERROR_TYPE
        
    def block(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        for i in range(1, len(types) - 1, 2):
            if types[i] == global_constants.ERROR_TYPE:
                line = (ctx.start.line, ctx.start.column)
                self.msgs_db.insert_error(line, 'Ocurre un error en el bloque')
                return global_constants.ERROR_TYPE
        
        return types[-3]    
    
    def while_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        line = (ctx.start.line, ctx.start.column)
        
        if self.cast_bool(types[1]) != basic_types.BOOL:
            self.msgs_db.insert_error(line, f'{types[1]} no es compatible con {basic_types.BOOL}')
            return global_constants.ERROR_TYPE
        
        if self.cast_bool(types[3]) != global_constants.ERROR_TYPE:
            return basic_types.OBJECT
        else:
            self.msgs_db.insert_error(line, 'Ocurre un error en el bloque')
            return global_constants.ERROR_TYPE
            
    def if_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.ERROR_TYPE, types)) or self.cast_bool(types[1]) != basic_types.BOOL:
            return global_constants.ERROR_TYPE
               
        return global_constants.NO_TYPE
    
    def let_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.ERROR_TYPE, types)):
            return global_constants.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column) 
        
        i = 1
        
        actual_type = None
        
        while ctx.children[i].getText().lower() != types_sys_constants.IN:
            if isinstance(ctx.children[i], YaplParser.ExprContext):
                if types[i] != actual_type:
                    self.msgs_db.insert_error(line, f'{types[i]} no es compatible con {actual_type}')
                    return global_constants.ERROR_TYPE
            elif ctx.children[i].symbol.type == typs.ID:
                if self.sym_table.exists(ctx.children[i].getText()) and self.sym_table.exists(ctx.children[i + 2].getText()):
                    actual_type = self.sym_table.get(ctx.children[i].getText()).typ
                else:
                    self.msgs_db.insert_error(line, f'{ctx.children[i].getText()} y/o {ctx.children[i + 2].getText()} no existe(n)')
                    return global_constants.ERROR_TYPE
                
            i += 1
            
        return types[-1]
                
    def id_lround(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        
        print(ctx.getText(), types, ctx.children[2].getText())
        if any(map(lambda x: x == global_constants.ERROR_TYPE, types)):
            return global_constants.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(ctx.children[0].getText()):
            elem: TableItem = self.sym_table.get(ctx.children[0].getText())
            
            comma_count = len(list(filter(lambda x: is_terminal_node(x) and  x.symbol.type == typs.COMMA, ctx.children)))
            param_count = 0
            
            if comma_count == 0:
                if is_terminal_node(ctx.children[2]):
                    param_count = 0
                else:
                    param_count = 1
            else:
                param_count = comma_count + 1
            
            if param_count != elem.param_num:
                self.msgs_db.insert_error(line, f'El numero de parametros no coincide con el numero de parametros del método')
                return global_constants.ERROR_TYPE
            
            table = self.sym_table.tables[self.sym_table.get_table_index(elem.lex)]
            
            indx = 2
            
            for i in range(elem.param_num):
                if table.items[i].typ != types[indx]:
                    self.msgs_db.insert_error(line, f'{table.items[i].typ} no es compatible con {types[indx]}')
                    return global_constants.ERROR_TYPE
                else:
                    indx += 2
            
            return elem.typ
        else:
            self.msgs_db.insert_error(line, f'{ctx.children[0].getText()} no existe')
            return global_constants.ERROR_TYPE
        
    def expr_point(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.ERROR_TYPE, types)):
            return global_constants.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(types[0]):
            table_index = self.sym_table.get_table_index(types[0])
            id_exists = self.sym_table.exists_in_table(table_index, ctx.children[2].getText())
            
            if id_exists:
                elem: TableItem = self.sym_table.get_from_table(table_index, ctx.children[2].getText())
                
                comma_count = len(list(filter(lambda x: is_terminal_node(x) and x.symbol.type == typs.COMMA, ctx.children)))
                param_count = 0
            
                if comma_count == 0:
                    if is_terminal_node(ctx.children[4]):
                        param_count = 0
                    else:
                        param_count = 1
                else:
                    param_count = comma_count + 1
                    
                
                if param_count != elem.param_num:
                    self.msgs_db.insert_error(line, f'El numero de parametros no coincide con el numero de parametros del método')
                    return global_constants.ERROR_TYPE
                
                table = self.sym_table.tables[self.sym_table.get_table_index(elem.lex)]
            
                indx = 4
                
                for i in range(elem.param_num):
                    if table.items[i].typ != types[indx]:
                        self.msgs_db.insert_error(line, f'{table.items[i].typ} no es compatible con {types[indx]}')
                        return global_constants.ERROR_TYPE
                    else:
                        indx += 2
                
                return elem.typ
            else:
                self.msgs_db.insert_error(line, f'{ctx.children[2].getText()} no existe')
                return global_constants.ERROR_TYPE
        else:
            self.msgs_db.insert_error(line, f'{types[0]} no existe')
            return global_constants.ERROR_TYPE
        
    def expr_arroba(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.ERROR_TYPE, types)):
            return global_constants.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(types[0]) and self.sym_table.exists(ctx.children[2].getText()):
            table_index = self.sym_table.get_table_index(types[0])
            id_exists = self.sym_table.exists_in_table(table_index, ctx.children[4].getText())
            
            if id_exists:
                elem: TableItem = self.sym_table.get_from_table(table_index, ctx.children[4].getText())
                
                comma_count = len(list(filter(lambda x: is_terminal_node(x) and x.symbol.type == typs.COMMA, ctx.children)))
                param_count = 0
            
                if comma_count == 0:
                    if is_terminal_node(ctx.children[6]):
                        param_count = 0
                    else:
                        param_count = 1
                else:
                    param_count = comma_count + 1
                
                if param_count != elem.param_num:
                    self.msgs_db.insert_error(line, f'El numero de parametros no coincide con el numero de parametros del método')
                    return global_constants.ERROR_TYPE
                
                table = self.sym_table.tables[self.sym_table.get_table_index(elem.lex)]
            
                indx = 6
                
                for i in range(elem.param_num):
                    if table.items[i].typ != types[indx]:
                        self.msgs_db.insert_error(line, f'{table.items[i].typ} no es compatible con {types[indx]}')
                        return global_constants.ERROR_TYPE
                    else:
                        indx += 2
                
                return elem.typ
            else:
                self.msgs_db.insert_error(line, f'{ctx.children[4].getText()} no existe')
                return global_constants.ERROR_TYPE
        else: 
            self.msgs_db.insert_error(line, f'{types[0]} o {ctx.children[2].getText()} no existe')
            return global_constants.ERROR_TYPE
            
        
        
            


types_sys = TypeSystem()
