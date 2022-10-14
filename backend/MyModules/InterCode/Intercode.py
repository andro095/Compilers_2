from pydantic import BaseModel

from Quadruples import Quadruples, make_quadruple
from SymbolTable import SymbolTable
from Global import global_constants
from YAPL import YaplParser

class InterCodeItem(BaseModel):
    dir: str | None = None
    code: str = ''

class InterCode:
    def __init__(self):
        self.__quadruples = Quadruples()
        self.symbol_table = SymbolTable()
        self.temps = 0
        self.let_count = 0
        self.tabs_counter = 1
        self.goto_labels_counter = 0
        self.object_counter = 0
        
        self.rules ={
            (global_constants.token_types.ID, global_constants.token_types.ASIGN): self.assign,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.ARROBA): self.expr_arroba,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.POINT): self.expr_point,
            (global_constants.token_types.ID, global_constants.token_types.LROUND): self.id_expr,
            (global_constants.token_types.IF, global_constants.sem_kinds.EXPR): self.if_expr,
            (global_constants.token_types.WHILE, global_constants.sem_kinds.EXPR): self.while_expr,
            (global_constants.token_types.LCURLY, global_constants.sem_kinds.EXPR): self.block,
            (global_constants.token_types.LET, global_constants.token_types.ID): self.let_expr,
            (global_constants.token_types.ISVOID, global_constants.sem_kinds.EXPR): self.is_void,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.ADD): self.op,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.SUB): self.op,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.MULTIPLY): self.op,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.DIVIDE): self.op,
            (global_constants.token_types.INT_NOT, global_constants.sem_kinds.EXPR): self.not_int,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.LESS_THAN): self.op,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.LESS_EQUAL): self.op,
            (global_constants.sem_kinds.EXPR, global_constants.token_types.EQUAL): self.op,
            (global_constants.token_types.NOT, global_constants.sem_kinds.EXPR): self.not_expr,
            (global_constants.token_types.LROUND, global_constants.sem_kinds.EXPR): self.lround_expr,
            
        }
    def dummy(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]):
        return InterCodeItem(dir='')
        
    def increase_tabs(self):
        self.tabs_counter += 1
    
    def decrease_tabs(self):
        self.tabs_counter -= 1
    
    def add_quadruple(self, op: str, arg1: str | None = None, arg2: str | None = None, result: str | None = None):
        self.__quadruples.add(make_quadruple(op=op, arg1=arg1, arg2=arg2, result=result))
        
    def print_quadruple(self):
        print(str(self.__quadruples))
        
    def get_base_type(self, ctx: YaplParser.ExprContext):
        inter_code_item = InterCodeItem()
        
        if ctx.children[0].symbol.type in global_constants.BASIC_TOKENS:
            inter_code_item.dir = f'{ctx.children[0].getText()}'   
        elif ctx.children[0].symbol.type == global_constants.token_types.ID:
            id_item = self.symbol_table.get(ctx.children[0].getText())
            class_name = self.symbol_table.tables[self.symbol_table.scopes[1]].name
            heap_or_stack = 'h' if id_item.mem_base == global_constants.base_memory.HEAP else 's'
            inter_code_item.dir = f'{class_name}_{heap_or_stack}[{id_item.mem_pos}]'
        elif ctx.children[0].symbol.type == global_constants.token_types.NEW:
            ob_item = self.symbol_table.get(f'obj{self.object_counter}')
            class_name = self.symbol_table.tables[self.symbol_table.scopes[1]].name
            heap_or_stack = 'h' if ob_item.mem_base == global_constants.base_memory.HEAP else 's'
            self.add_quadruple(op = 'allocate', arg1=f'{ob_item.byte_size}', arg2=f'<{ob_item.typ}>', result=f'{class_name}_{heap_or_stack}[{ob_item.mem_pos}]')
            inter_code_item.dir = f'{class_name}_{heap_or_stack}[{ob_item.mem_pos}]'
            inter_code_item.code = self.tabs_counter * '\t' + f'{class_name}_{heap_or_stack}[{ob_item.mem_pos}] = allocate {ob_item.byte_size} <{ob_item.typ}>'
            self.object_counter += 1
        
        return inter_code_item    
        
    def evaluate_program(self, ctx, intercodes: list[InterCodeItem]):
        inter_code_item = InterCodeItem(dir='Program', code='Program:' + '\n' + self.tabs_counter * "\t" + 'goto Main.main')
        for intercode in intercodes:
            inter_code_item.code += '\n' +  self.tabs_counter * "\t" + intercode.dir + intercode.code
            
        self.add_quadruple(op=inter_code_item.dir)
        
        return inter_code_item
    
    def evaluate_class(self, ctx, intercodes: list[InterCodeItem]):
        
        class_item = self.symbol_table.get(ctx.children[1].getText())
        
        inter_code_item = InterCodeItem(dir=f'{class_item.lex}:', code='')
        
        for intercode in intercodes:
            if intercode.dir is None:
                inter_code_item.code += '\n' + intercode.code
            else:
                inter_code_item.code += '\n' + self.tabs_counter * "\t" + intercode.dir + ':' + intercode.code
            
        inter_code_item.code += '\n' + (self.tabs_counter - 1) * "\t" + f'End {class_item.lex}' + '\n'
        self.add_quadruple(op=inter_code_item.dir)
        
        return inter_code_item
    
    def evaluate_feature(self, ctx, intercodes: list[InterCodeItem]):
        
        feature_item = self.symbol_table.get(ctx.children[0].getText())
        
        inter_code_item = None
        
        if feature_item.sem_kind == global_constants.sem_kinds.ATTR:
            if len(ctx.children) > 3:
                inter_code_item = InterCodeItem(code='')
                
                for intercode in intercodes:
                    inter_code_item.code += intercode.code
                    
                class_name = self.symbol_table.tables[self.symbol_table.scopes[1]].name
                heap_or_stack = 'h' if feature_item.mem_base == global_constants.base_memory.HEAP else 's'
                
                inter_code_item.code += ('\n' if intercodes[0].code != '' else '') + self.tabs_counter * "\t" + f'{class_name}_{heap_or_stack}[{feature_item.mem_pos}] = {intercodes[0].dir}'
                self.add_quadruple(op='=', arg1=intercodes[0].dir, result=f'{class_name}_{heap_or_stack}[{feature_item.mem_pos}]')
        else:
            
            inter_code_item = InterCodeItem(dir=f'{self.symbol_table.actual_scope_name}.{feature_item.lex}', code='')
            
            for intercode in intercodes:
                if intercode.code != '':
                    inter_code_item.code += '\n' + intercode.code
            
            if intercodes[0].dir != '':    
                inter_code_item.code += '\n' + self.tabs_counter * '\t' + 'return ' + intercodes[0].dir
                self.add_quadruple(op='return', arg1=intercodes[0].dir)
            inter_code_item.code += '\n' + (self.tabs_counter - 1) * '\t' + 'End ' + inter_code_item.dir
            
            self.add_quadruple(op='End ' + inter_code_item.dir)
            self.add_quadruple(op=inter_code_item.dir)
            
            
        return inter_code_item
            
    def get_key_tuple(self, ctx: YaplParser.ExprContext, res: list[bool]) -> tuple:
        elem0 = global_constants.sem_kinds.EXPR if not res[0] else ctx.children[0].symbol.type
        elem1 = global_constants.sem_kinds.EXPR if not res[1] else ctx.children[1].symbol.type
        return (elem0, elem1)   
    
    def evaluate_expr(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem], res: list[bool]) -> InterCodeItem:
        return self.rules[self.get_key_tuple(ctx, res)](ctx, intercodes)     
        
    def op(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        operator = global_constants.op_dict[ctx.children[1].symbol.type]
        self.add_quadruple(op=operator, arg1=intercodes[0].dir, arg2=intercodes[1].dir, result=f't{self.temps}')
        inter_code_item = InterCodeItem(dir=f't{self.temps}', code='')
        
        inter_code_item.code += intercodes[0].code + ('\n' if intercodes[0].code != '' else '') + intercodes[1].code
        inter_code_item.code += ('\n' if intercodes[1].code != '' else '') + self.tabs_counter * '\t' + f't{self.temps} = {intercodes[0].dir} {operator} {intercodes[1].dir}'
        
        self.temps += 1
        
        return inter_code_item
    
    def not_int(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        self.add_quadruple(op='*', arg1=intercodes[0].dir, arg2='-1', result=f't{self.temps}')
        inter_code_item = InterCodeItem(dir=f't{self.temps}', code='')
        
        inter_code_item.code += intercodes[0].code
        inter_code_item.code += ('\n' if intercodes[0].code != '' else '')  + self.tabs_counter * '\t' + f't{self.temps} = {intercodes[0].dir} * -1'
        
        self.temps += 1
        
        return inter_code_item
    
    def not_expr(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        self.add_quadruple(op='not', arg1=intercodes[0].dir, result=f't{self.temps}')
        inter_code_item = InterCodeItem(dir=f't{self.temps}', code='')
        
        inter_code_item.code += intercodes[0].code
        inter_code_item.code += ('\n' if intercodes[0].code != '' else '')  + self.tabs_counter * '\t' + f't{self.temps} = not {intercodes[0].dir}'
        
        self.temps += 1
        
        return inter_code_item
    
    def lround_expr(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        return InterCodeItem(dir=intercodes[0].dir, code=intercodes[0].code)
    
    def assign(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        expr_item = self.symbol_table.get(ctx.children[0].getText())
        
        class_name = self.symbol_table.tables[self.symbol_table.scopes[1]].name
        heap_or_stack = 'h' if expr_item.mem_base == global_constants.base_memory.HEAP else 's'
        
        self.add_quadruple(op='=', arg1=intercodes[0].dir, result=f'{class_name}_{heap_or_stack}[{expr_item.mem_pos}]')
        inter_code_item = InterCodeItem(dir=f'{class_name}_{heap_or_stack}[{expr_item.mem_pos}]', code='')
        
        inter_code_item.code += intercodes[0].code
        inter_code_item.code += ('\n' if intercodes[0].code != '' else '')  + self.tabs_counter * '\t' + f'{class_name}_{heap_or_stack}[{expr_item.mem_pos}] = {intercodes[0].dir}'
        
        return inter_code_item
    
    def is_void(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        inter_code_item = InterCodeItem(dir=f't{self.temps}', code=intercodes[0].code)
        
        inter_code_item.code += ('\n' if intercodes[0].code != '' else '') + self.tabs_counter * '\t' + f't{self.temps} = {intercodes[0].dir} == null'
        self.add_quadruple(op='==', arg1=intercodes[0].dir, result=f't{self.temps}')
        
        self.temps += 1
        
        return inter_code_item
    
    def if_expr(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        inter_code_item = InterCodeItem(dir='', code='')
        
        intercodes[0].code = intercodes[0].code.replace(self.tabs_counter * '\t', (self.tabs_counter - 1) * '\t')
        
        inter_code_item.code += intercodes[0].code
        inter_code_item.code += ('\n' if intercodes[0].code != '' else '') + self.tabs_counter * '\t' + f'ifFalse {intercodes[0].dir} goto L{self.goto_labels_counter}' + '\n'
        self.add_quadruple(op='ifFalse', arg1=intercodes[0].dir, arg2='goto' ,result=f'L{self.goto_labels_counter}')
        inter_code_item.code += intercodes[1].code
        inter_code_item.code += ('\n' if intercodes[1].code != '' else '')  + self.tabs_counter * '\t' + f'goto L{self.goto_labels_counter + 1}'
        self.add_quadruple(op='goto', result=f'L{self.goto_labels_counter + 1}')
        inter_code_item.code += '\n' + self.tabs_counter * '\t' + f'L{self.goto_labels_counter}:' + '\n'
        self.add_quadruple(op=f'L{self.goto_labels_counter}:')
        inter_code_item.code += intercodes[2].code
        self.goto_labels_counter += 1
        inter_code_item.code += ('\n' if intercodes[2].code != '' else '')  + self.tabs_counter * '\t' + f'L{self.goto_labels_counter}:'
        self.add_quadruple(op=f'L{self.goto_labels_counter}:')
        self.goto_labels_counter += 1
        
        return inter_code_item
    
    def block(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        inter_code_item = InterCodeItem(dir=intercodes[-1].dir, code='')
        
        for i, intercode in enumerate(intercodes):
            if intercode.code != '':
                inter_code_item.code += ('\n' if i != 0 else '') + intercode.code
            
        if intercodes[-1].code == '':
            inter_code_item.code += '\n' + self.tabs_counter * "\t" + f't{self.temps} = {intercodes[-1].dir}'
            self.temps += 1
        
        return inter_code_item
    
    def while_expr(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        inter_code_item = InterCodeItem(dir=intercodes[1].dir, code='')
        
        intercodes[0].code = intercodes[0].code.replace(self.tabs_counter * '\t', (self.tabs_counter - 1) * '\t')
        
        inter_code_item.code += intercodes[0].code
        inter_code_item.code += ('\n' if intercodes[0].code != '' else '')  + self.tabs_counter * '\t' + f'L{self.goto_labels_counter}:'
        self.add_quadruple(op=f'L{self.goto_labels_counter}:')
        inter_code_item.code += '\n' + self.tabs_counter * '\t' + f'ifFalse {intercodes[0].dir} goto L{self.goto_labels_counter + 1}' + '\n'
        self.add_quadruple(op='ifFalse', arg1=intercodes[0].dir, arg2='goto' ,result=f'L{self.goto_labels_counter + 1}')
        inter_code_item.code += intercodes[1].code
        inter_code_item.code += ('\n' if intercodes[1].code != '' else '')  + self.tabs_counter * '\t' + f'goto L{self.goto_labels_counter}'
        self.add_quadruple(op='goto', result=f'L{self.goto_labels_counter}')
        self.goto_labels_counter += 1
        inter_code_item.code += '\n' + self.tabs_counter * '\t' + f'L{self.goto_labels_counter}:'
        self.add_quadruple(op=f'L{self.goto_labels_counter}:')
        self.goto_labels_counter += 1
        
        return inter_code_item
    
    def id_expr(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        inter_code_item = InterCodeItem(dir=f't{self.temps}', code='')
        
        method_item = self.symbol_table.get(ctx.children[0].getText())
        
        for i, intercode in enumerate(intercodes):
            inter_code_item.code += intercode.code + ('\n' if intercode.code != '' else '')
            
        for i, intercode in enumerate(intercodes):
            inter_code_item.code += ('\n' if i != 0 else '') + self.tabs_counter * '\t' + 'param ' + intercode.dir
            self.add_quadruple(op='param', result=intercode.dir)
                
        
        inter_code_item.code += ('\n' if len(intercodes) > 0 else '') + self.tabs_counter * '\t' + f't{self.temps} = call {self.symbol_table.tables[self.symbol_table.scopes[1]].name}.{method_item.lex}, {len(intercodes)}'
        
        self.add_quadruple(op='call', arg1=f'{self.symbol_table.tables[self.symbol_table.scopes[1]].name}.{method_item.lex}', arg2=len(intercodes), result=f't{self.temps}')
        
        self.temps += 1
        
        return inter_code_item
    
    def expr_point(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        inter_code_item = InterCodeItem(dir='', code='')
        
        
        my_dir = f'{intercodes[0].dir}'
        
        if intercodes[0].code == '':
            inter_code_item.code += self.tabs_counter * '\t' + f't{self.temps} = {intercodes[0].dir}' + '\n'
            self.add_quadruple(op='=', arg1=intercodes[0].dir, result=f't{self.temps}')
            my_dir = f't{self.temps}'
            self.temps += 1
        
        inter_code_item.dir = f'{intercodes[0].dir}' if intercodes[0].code != '' else f't{self.temps}'
        
        for i, intercode in enumerate(intercodes):
            inter_code_item.code += intercode.code + ('\n' if intercode.code != '' else '')
            
        for i, intercode in enumerate(intercodes):
            if i != 0:
                inter_code_item.code += ('\n' if i != 1 else '') + self.tabs_counter * '\t' + 'param ' + intercode.dir
                self.add_quadruple(op='param', result=intercode.dir)
            
            
        inter_code_item.code += ('\n' if len(intercodes) > 1 else '') + self.tabs_counter * '\t' + f'{my_dir} = call {ctx.children[0].r_type}.{ctx.children[2].getText()}, {len(intercodes) - 1}'
        
        self.add_quadruple(op='call', arg1=f'{ctx.children[0].r_type}.{ctx.children[2].getText()}', arg2=len(intercodes), result=f'{my_dir}')
        
        
        return inter_code_item
    
    def expr_arroba(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem:
        inter_code_item = InterCodeItem(dir='', code='')
        
        type_expr = ctx.children[2].getText()
        
        inter_code_item.dir = f'{intercodes[0].dir}' if intercodes[0].code != '' else f't{self.temps}'
        
        my_dir = f'{intercodes[0].dir}'
        
        if intercodes[0].code == '':
            my_dir = f't{self.temps}'
            inter_code_item.code += self.tabs_counter * '\t' + f't{self.temps} = {intercodes[0].dir}' + '\n'
            self.add_quadruple(op='=', arg1=intercodes[0].dir, result=f't{self.temps}')
            self.temps += 1
        
        for i, intercode in enumerate(intercodes):
            inter_code_item.code += intercode.code + ('\n' if intercode.code != '' else '')
            
        for i, intercode in enumerate(intercodes):
            if i != 0:
                inter_code_item.code += ('\n' if i != 1 else '') + self.tabs_counter * '\t' + 'param ' + intercode.dir
                self.add_quadruple(op='param', result=intercode.dir)
            
            
        inter_code_item.code += ('\n' if len(intercodes) > 1 else '') + self.tabs_counter * '\t' + f'{my_dir} = call {type_expr}.{ctx.children[4].getText()}, {len(intercodes) - 1}'
        
        self.add_quadruple(op='call', arg1=f'{type_expr}.{ctx.children[4].getText()}', arg2=len(intercodes), result=f'{my_dir}')
        
        
        return inter_code_item
        
        
    def let_expr(self, ctx: YaplParser.ExprContext, intercodes: list[InterCodeItem]) -> InterCodeItem: 
        inter_code_item = InterCodeItem(dir=f'{intercodes[-1].dir}')
        
        
        for i, intercode in enumerate(intercodes):
            if intercode.code != '':
                inter_code_item.code += intercode.code + ('\n' if i != len(intercodes) - 1 else '')
                
        return inter_code_item