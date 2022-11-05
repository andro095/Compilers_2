import re

# Librerías de terceros
from pydantic import BaseModel
from tabulate import tabulate

# Librerías propias
from Singleton import MySingleton

# Liberías de locales
from .Constants import constants

class Quadruple(BaseModel):
    """ 
    Clase que representa un cuádruplo.
    """
    op: str
    arg1: str | None = ''
    arg2: str | None = ''
    result: str | None = ''
    
    
def make_quadruple(op: str, arg1: str | None = None, arg2: str | None = None, result: str | None = None) -> Quadruple:
    """ 
    Función que crea un cuádruplo.
    """
    return Quadruple(op=op, arg1=arg1, arg2=arg2, result=result)

class Quadruples(metaclass=MySingleton):
    def __init__(self):
        self.__quadruples: Quadruple = []
        self.obj_code =  ''
        
    def add(self, quadruple: Quadruple):
        self.__quadruples.append(quadruple)
    
    def get_arg_repr(self, arg: str, temp_addr: int) -> str:
        if re.match(constants.regrexes.INTEGER, arg):
            return f'li $t{temp_addr}, {arg}\n'
        elif re.match(constants.regrexes.STRING, arg):
            return arg
        elif re.match(constants.regrexes.MEM_POS, arg):
            index_open_square_bracket = arg.find('[')
            
            return f'lw $t{temp_addr}, {arg[index_open_square_bracket + 1:-1]}($28)\n'
        elif re.match(constants.regrexes.TEMPS, arg):
            return f'lw $t{temp_addr}, {500+int(arg[1:])*4}($28)\n'
        
    def get_result_repr(self, result: str) -> str:
        
        if re.match(constants.regrexes.MEM_POS, result):
            index_open_square_bracket = result.find('[')
            
            return f'{result[index_open_square_bracket + 1:-1]}'
        elif re.match(constants.regrexes.TEMPS, result):
            return f'{500+int(result[1:])*4}'
        
    def convert(self):
        for index, quadruple in enumerate(self.__quadruples):
            if quadruple.op in constants.operators.arimetic_opeators:
                arg_1_repr = self.get_arg_repr(quadruple.arg1, 0)
                arg_2_repr = self.get_arg_repr(quadruple.arg2, 1)
                result_repr = self.get_result_repr(quadruple.result)
                self.obj_code += arg_1_repr + arg_2_repr
                self.obj_code += f'{constants.operators.arimetic_opeators[quadruple.op]} $t2, $t0, $t1\n'
                self.obj_code += f'sw $t2, {result_repr}($28)\n'
                
            elif quadruple.op == 'goto':
                self.obj_code += f'j {quadruple.arg1}\n'
                
            elif quadruple.op == 'label':
                self.obj_code += f'{quadruple.arg1}:\n'     
                
    
    def __str__(self) -> None:
        tab = tabulate(map(lambda x: x.dict(), self.__quadruples), headers='keys')
        mystr = f'\nCuádruplos:\n{tab}'
        
        return mystr
    
    def reset(self):
        self.__quadruples = []
        self.obj_code =  ''