
# Librerías de terceros
from pydantic import BaseModel
from tabulate import tabulate

# Librerías propias
from Singleton import MySingleton

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
        self.__quadruples = []
        
    def add(self, quadruple: Quadruple):
        self.__quadruples.append(quadruple)
        
    def __str__(self) -> None:
        tab = tabulate(map(lambda x: x.dict(), self.__quadruples), headers='keys')
        mystr = f'\nCuádruplos:\n{tab}'
        
        return mystr