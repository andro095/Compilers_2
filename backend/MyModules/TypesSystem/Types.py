from ConsoleMessages import MessagesDB
from SymbolTable import SymbolTable, TableItem
from YAPL import YaplParser
from antlr4.tree.Tree import TerminalNodeImpl

from Global import global_constants

def is_terminal_node(node) -> bool:
    return isinstance(node, TerminalNodeImpl)

class TypeSystem:
    def __init__(self):
        self.msgs_db = MessagesDB()
        
        self.rules ={
            (global_constants.token_types.ID, global_constants.token_types.ASIGN): self.assign,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.ARROBA): self.expr_arroba,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.POINT): self.expr_point,
            (global_constants.token_types.ID, global_constants.token_types.LROUND): self.id_lround,
            (global_constants.token_types.IF, global_constants.sem_kinds.EXPR): self.if_expr,
            (global_constants.token_types.WHILE, global_constants.sem_kinds.EXPR): self.while_expr,
            (global_constants.token_types.LCURLY, global_constants.sem_kinds.EXPR): self.block,
            (global_constants.token_types.LET, global_constants.token_types.ID): self.let_expr,
            (global_constants.token_types.ISVOID, global_constants.sem_kinds.EXPR): self.is_void,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.ADD): self.arimetic,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.SUB): self.arimetic,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.MULTIPLY): self.arimetic,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.DIVIDE): self.arimetic,
            (global_constants.token_types.INT_NOT, global_constants.sem_kinds.EXPR): self.not_int,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.LESS_THAN): self.compare,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.LESS_EQUAL): self.compare,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.EQUAL): self.compare,
            (global_constants.token_types.NOT, global_constants.sem_kinds.EXPR): self.not_expr,
            (global_constants.token_types.LROUND, global_constants.sem_kinds.EXPR): self.lround_expr,
            
        }
        self.sym_table = SymbolTable()
        
    def get_father(self, clas: str) -> str:
        table_item = self.sym_table.get(clas)
        return table_item.inherits if table_item.inherits is not None else clas
    
    def cast_int(self, clas: str) -> str:
        return global_constants.basic_types.INT if clas == global_constants.basic_types.BOOL else clas
    
    def cast_bool(self, clas: str) -> str:
        return global_constants.basic_types.BOOL if clas == global_constants.basic_types.INT else clas
        
    def get_base_case_type(self, ctx: YaplParser.ExprContext) -> str:              
        if ctx.children[0].symbol.type == global_constants.token_types.NEW:
            return ctx.children[1].getText() if self.sym_table.exists(ctx.children[1].getText()) else global_constants.results_types.ERROR_TYPE
        elif ctx.children[0].symbol.type == global_constants.token_types.ID:
            if self.sym_table.exists(ctx.children[0].getText()):
                elem: TableItem = self.sym_table.get(ctx.children[0].getText())
                if elem.sem_kind == global_constants.sem_kinds.ATTR or elem.sem_kind == global_constants.sem_kinds.PARAMETER:
                    if ctx.getChildCount() == 1:
                        return elem.typ
                    elif ctx.children[1].symbol.type == global_constants.token_types.POINT or ctx.children[1].symbol.type == global_constants.token_types.ASIGN:
                        return elem.typ
                    else:
                        line = (ctx.start.line, ctx.start.column)
                        self.msgs_db.insert_errror(line, f'No se puede acceder a {ctx.children[1].getText()} de una variable.')
                        return global_constants.results_types.ERROR_TYPE
                elif elem.sem_kind == global_constants.sem_kinds.METHOD:
                    if ctx.getChildCount() > 1 and ctx.children[1].symbol.type == global_constants.token_types.LROUND:
                        return elem.typ
                    else: 
                        line = (ctx.start.line, ctx.start.column)
                        self.msgs_db.insert_error(line, f'No se declaró bien el método {ctx.children[0].getText()}.')
                        return global_constants.results_types.ERROR_TYPE
            else:
                line = (ctx.start.line, ctx.start.column)
                self.msgs_db.insert_error(line, f'{ctx.children[0].getText()} no existe.')
                return global_constants.results_types.ERROR_TYPE
        elif ctx.children[0].symbol.type == global_constants.token_types.INTEGER:
            return global_constants.basic_types.INT
        elif ctx.children[0].symbol.type == global_constants.token_types.STRING:
            return global_constants.basic_types.STRING
        elif ctx.children[0].symbol.type == global_constants.token_types.TRUE or ctx.children[0].symbol.type == global_constants.token_types.FALSE:
            return global_constants.basic_types.BOOL
    
    def get_key_tuple(self, ctx: YaplParser.ExprContext, res: list[bool]) -> tuple:
        elem0 = global_constants.sem_kinds.EXPR if not res[0] else ctx.children[0].symbol.type
        elem1 = global_constants.sem_kinds.EXPR if not res[1] else ctx.children[1].symbol.type
        return (elem0, elem1)
    
    def validate_feature(self, ctx: YaplParser.FeatureContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.results_types.ERROR_TYPE, types)):
            return global_constants.results_types.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(ctx.children[0].getText()):
            feature_item = self.sym_table.get(ctx.children[0].getText())
            if feature_item.sem_kind == global_constants.sem_kinds.ATTR:
                
                if ctx.children[2].getText() == global_constants.basic_types.SELF_TYPE:
                    return global_constants.results_types.CHECK_TYPE
                
                if not self.sym_table.exists(ctx.children[2].getText()):
                    self.msgs_db.insert_error(line, f'El tipo {ctx.children[2].getText()} no existe.')
                    return global_constants.results_types.ERROR_TYPE
                
                if ctx.getChildCount() == 3:
                    return global_constants.results_types.CHECK_TYPE
                
                if types[4] != feature_item.typ and types[4] != global_constants.basic_types.SELF_TYPE:
                    if self.sym_table.inherits_from(feature_item.typ, types[4]):
                        return global_constants.results_types.CHECK_TYPE
                    
                    self.msgs_db.insert_error(line, f'El tipo de la variable {ctx.children[4].getText()}: {types[4]}, no es del mismo tipo que {feature_item.lex}: {feature_item.typ}.')
                    return global_constants.results_types.ERROR_TYPE
                else:
                    return global_constants.results_types.CHECK_TYPE
            elif feature_item.sem_kind == global_constants.sem_kinds.METHOD:
                if ctx.children[-4].getText() != global_constants.basic_types.SELF_TYPE and not self.sym_table.exists(ctx.children[-4].getText()):
                    self.msgs_db.insert_error(line, f'El tipo del metodo {ctx.children[0].getText()}: {ctx.children[-4].getText()} no está declarado.')
                    return global_constants.results_types.ERROR_TYPE
                
                if types[-2] == None:
                    self.msgs_db.insert_error(line, f'Sin tipo')
                    return global_constants.results_types.ERROR_TYPE
                
                if types[-2] != feature_item.typ and types[-2] != global_constants.results_types.NO_TYPE:
                    self.msgs_db.insert_error(line, f'Tipo de retorno de la expresión: {types[-2]} no es compatible con el tipo del retorno de la función {feature_item.lex}: {feature_item.typ}.')
                    return global_constants.results_types.ERROR_TYPE
                else:
                    return global_constants.results_types.CHECK_TYPE
        else:
            self.msgs_db.insert_error(line, f'La característica {ctx.children[0].getText()} no existe.')
            return global_constants.results_types.ERROR_TYPE
        
    def validate_expr(self, ctx: YaplParser.ExprContext, types: list[str] ,res: list[bool]) -> str:
        return self.rules[self.get_key_tuple(ctx, res)](ctx, types)
    
    def validate_formal(self, ctx: YaplParser.FormalContext) -> str:
        if self.sym_table.exists(ctx.children[0].getText()) and self.sym_table.exists(ctx.children[2].getText()):
            return global_constants.results_types.CHECK_TYPE
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msgs_db.insert_error(line, f'Parametro {ctx.children[0].getText()} y/o tipo {ctx.children[2].getText()} no está declarado.')
            return global_constants.results_types.ERROR_TYPE
        
    def lround_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        return types[1]
    
    def is_void(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        return global_constants.basic_types.BOOL if types[1] != global_constants.results_types.ERROR_TYPE else global_constants.results_types.ERROR_TYPE
    
    def compare(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:        
        if types[0] == global_constants.results_types.ERROR_TYPE or types[2] == global_constants.results_types.ERROR_TYPE:
            return global_constants.results_types.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(types[0]) and self.sym_table.exists(types[2]):
            if types[0] == types[2]:
                return global_constants.basic_types.BOOL
            else:
                father0 = self.get_father(types[0])
                father2 = self.get_father(types[2])
                
                if father0 == father2 or types[0] == father2 or types[2] == father0:
                    return global_constants.basic_types.BOOL
                else:
                    self.msgs_db.insert_error(line, f'El tipo de la parte izquierda: {types[0]} no es compatible con la de la parte derecha: {types[2]}.')
                    return global_constants.results_types.ERROR_TYPE
        else: 
            self.msgs_db.insert_error(line, f'El tipo {types[0]} y/o {types[2]} no existe(n).')
            return global_constants.results_types.ERROR_TYPE
            
    def not_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if self.cast_bool(types[1]) == global_constants.basic_types.BOOL:
            return global_constants.basic_types.BOOL
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msgs_db.insert_error(line, f'El tipo de retorno de la expresión no es de tipo {global_constants.basic_types.BOOL}.')
            return global_constants.results_types.ERROR_TYPE
    
    def arimetic(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if self.cast_int(types[0]) == global_constants.basic_types.INT and self.cast_int(types[2]) == global_constants.basic_types.INT:
            return global_constants.basic_types.INT
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msgs_db.insert_error(line, f'El tipo de la expresión izquierda: {types[0]} y/o de la expresión derecha: {types[2]} no es(son) entero(s).')
            return global_constants.results_types.ERROR_TYPE
    
    def not_int(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if self.cast_int(types[1]) == global_constants.basic_types.INT:
            return global_constants.basic_types.INT
        else:
            line = (ctx.start.line, ctx.start.column)
            self.msgs_db.insert_error(line, f'El tipo de la expresión: {types[1]} no es de tipo {global_constants.basic_types.INT}.')
            return global_constants.results_types.ERROR_TYPE
            
    
    def assign(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if types[0] == global_constants.results_types.ERROR_TYPE or types[2] == global_constants.results_types.ERROR_TYPE:
            return global_constants.results_types.ERROR_TYPE
    
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
                    self.msgs_db.insert_error(line, f'El tipo de la expresión: {types[2]} no se le puede asignar a la variable {id_item.lex} de tipo {id_item.typ}.')
                    return global_constants.results_types.ERROR_TYPE
        else:
            self.msgs_db.insert_error(line, f'La variable {ctx.children[0].getText()} y/o el tipo de la expresión: {types[2]} no existe(n).')
            return global_constants.results_types.ERROR_TYPE
        
    def block(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        for i in range(1, len(types) - 1, 2):
            if types[i] == global_constants.results_types.ERROR_TYPE:
                line = (ctx.start.line, ctx.start.column)
                self.msgs_db.insert_error(line, 'Ocurre un error en el bloque')
                return global_constants.results_types.ERROR_TYPE
        
        return types[-3]    
    
    def while_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        line = (ctx.start.line, ctx.start.column)
        
        if self.cast_bool(types[1]) != global_constants.basic_types.BOOL:
            self.msgs_db.insert_error(line, f'El tipo de la condicional {types[1]} no es de tipo {global_constants.basic_types.BOOL}.')
            return global_constants.results_types.ERROR_TYPE
        
        if self.cast_bool(types[3]) != global_constants.results_types.ERROR_TYPE:
            return global_constants.basic_types.OBJECT
        else:
            self.msgs_db.insert_error(line, 'Ocurre un error en la expresión de retorno.')
            return global_constants.results_types.ERROR_TYPE
            
    def if_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.results_types.ERROR_TYPE, types)) or self.cast_bool(types[1]) != global_constants.basic_types.BOOL:
            return global_constants.results_types.ERROR_TYPE
               
        return global_constants.results_types.NO_TYPE
    
    def let_expr(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.results_types.ERROR_TYPE, types)):
            return global_constants.results_types.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column) 
        
        i = 1
        
        actual_type = None
        
        while ctx.children[i].getText().lower() != global_constants.string_cons.IN:
            if isinstance(ctx.children[i], YaplParser.ExprContext):
                if types[i] != actual_type:
                    self.msgs_db.insert_error(line, f'El tipo de la expresión: {types[i]} no es del tipo esperado: {actual_type}.')
                    return global_constants.results_types.ERROR_TYPE
            elif ctx.children[i].symbol.type == global_constants.token_types.ID:
                if self.sym_table.exists(ctx.children[i].getText()) and self.sym_table.exists(ctx.children[i + 2].getText()):
                    actual_type = self.sym_table.get(ctx.children[i].getText()).typ
                else:
                    self.msgs_db.insert_error(line, f'{ctx.children[i].getText()} y/o {ctx.children[i + 2].getText()} no existe(n).')
                    return global_constants.results_types.ERROR_TYPE
                
            i += 1
            
        return types[-1]
                
    def id_lround(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.results_types.ERROR_TYPE, types)):
            return global_constants.results_types.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(ctx.children[0].getText()):
            elem: TableItem = self.sym_table.get(ctx.children[0].getText())
            
            comma_count = len(list(filter(lambda x: is_terminal_node(x) and  x.symbol.type == global_constants.token_types.COMMA, ctx.children)))
            param_count = 0
            
            if comma_count == 0:
                if is_terminal_node(ctx.children[2]):
                    param_count = 0
                else:
                    param_count = 1
            else:
                param_count = comma_count + 1
            
            if param_count != elem.param_num:
                self.msgs_db.insert_error(line, f'El número de parametros no coincide con el numero de parametros del método {elem.lex}.')
                return global_constants.results_types.ERROR_TYPE
            
            table = self.sym_table.tables[self.sym_table.get_table_index(elem.lex)]
            
            indx = 2
            
            for i in range(elem.param_num):
                if table.items[i].typ != types[indx]:
                    self.msgs_db.insert_error(line, f'El tipo de la expresión: {types[indx]} no es del tipo esperado para el parámetro {table.items[i].lex}: {table.items[i].typ}.')
                    return global_constants.results_types.ERROR_TYPE
                else:
                    indx += 2
            
            return elem.typ
        else:
            self.msgs_db.insert_error(line, f'El método {ctx.children[0].getText()} no existe.')
            return global_constants.results_types.ERROR_TYPE
        
    def expr_point(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.results_types.ERROR_TYPE, types)):
            return global_constants.results_types.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(types[0]):
            table_index = self.sym_table.get_table_index(types[0])
            id_exists = self.sym_table.exists_in_table(table_index, ctx.children[2].getText())
            
            if len(ctx.children) < 5:
                self.msgs_db.insert_error(line, 'No se declaro bien la llamada al método.', 'sintáctico')
                return global_constants.results_types.ERROR_TYPE
            
            if id_exists:
                elem: TableItem = self.sym_table.get_from_table(table_index, ctx.children[2].getText())
                
                comma_count = len(list(filter(lambda x: is_terminal_node(x) and x.symbol.type == global_constants.token_types.COMMA, ctx.children)))
                param_count = 0
            
                if comma_count == 0:
                    if is_terminal_node(ctx.children[4]):
                        param_count = 0
                    else:
                        param_count = 1
                else:
                    param_count = comma_count + 1
                    
                
                if param_count != elem.param_num:
                    self.msgs_db.insert_error(line, f'El número de parametros no coincide con el numero de parametros del método {elem.lex}.')
                    return global_constants.results_types.ERROR_TYPE
                
                table = self.sym_table.tables[self.sym_table.get_table_index(elem.lex)]
            
                indx = 4
                
                for i in range(elem.param_num):
                    if table.items[i].typ != types[indx]:
                        self.msgs_db.insert_error(line, f'El tipo de la expresión: {types[indx]} no es del tipo esperado para el parámetro {table.items[i].lex}: {table.items[i].typ}.')
                        return global_constants.results_types.ERROR_TYPE
                    else:
                        indx += 2
                
                return elem.typ
            else:
                self.msgs_db.insert_error(line, f'El método {ctx.children[2].getText()} no existe.')
                return global_constants.results_types.ERROR_TYPE
        else:
            self.msgs_db.insert_error(line, f'El tipo de la expresión {types[0]} no existe.')
            return global_constants.results_types.ERROR_TYPE
        
    def expr_arroba(self, ctx: YaplParser.ExprContext, types: list[str]) -> str:
        if any(map(lambda x: x == global_constants.results_types.ERROR_TYPE, types)):
            return global_constants.results_types.ERROR_TYPE
        
        line = (ctx.start.line, ctx.start.column)
        
        if self.sym_table.exists(types[0]) and self.sym_table.exists(ctx.children[2].getText()):
            if not self.sym_table.inherits_from(types[0], ctx.children[2].getText()):
                
                msg = f'El tipo de la expresión, {types[0]}, no hereda de {ctx.children[2].getText()}.'
                
                if types[0] == ctx.children[2].getText():
                    msg = f'El tipo de la expresión, {types[0]}, no hereda de si mismo.'
                
                self.msgs_db.insert_error(line, msg)
                return global_constants.results_types.ERROR_TYPE
            
            table_index = self.sym_table.get_table_index(ctx.children[2].getText())
            id_exists = self.sym_table.exists_in_table(table_index, ctx.children[4].getText())
            
            if len(ctx.children) < 7:
                self.msgs_db.insert_error(line, 'No se declaro bien la llamada al método.', 'sintáctico')
                return global_constants.results_types.ERROR_TYPE
            
            if id_exists:
                elem: TableItem = self.sym_table.get_from_table(table_index, ctx.children[4].getText())
                
                comma_count = len(list(filter(lambda x: is_terminal_node(x) and x.symbol.type == global_constants.token_types.COMMA, ctx.children)))
                param_count = 0
            
                if comma_count == 0:
                    if is_terminal_node(ctx.children[6]):
                        param_count = 0
                    else:
                        param_count = 1
                else:
                    param_count = comma_count + 1
                
                if param_count != elem.param_num:
                    self.msgs_db.insert_error(line, f'El número de parametros no coincide con el numero de parametros del método {elem.lex}.')
                    return global_constants.results_types.ERROR_TYPE
                
                table = self.sym_table.tables[self.sym_table.get_table_index(elem.lex)]
            
                indx = 6
                
                for i in range(elem.param_num):
                    if table.items[i].typ != types[indx]:
                        self.msgs_db.insert_error(line, f'El tipo de la expresión, {types[indx]}, no es del tipo esperado para el parámetro {table.items[i].lex}: {table.items[i].typ}.')
                        return global_constants.results_types.ERROR_TYPE
                    else:
                        indx += 2
                
                return types[0]
            else:
                self.msgs_db.insert_error(line, f'El método {ctx.children[4].getText()} no existe.')
                return global_constants.results_types.ERROR_TYPE
        else: 
            self.msgs_db.insert_error(line, f'El tipo de la expresión {types[0]} o el tipo {ctx.children[2].getText()} no existe.')
            return global_constants.results_types.ERROR_TYPE
            
        
        
            


types_sys = TypeSystem()
