from pydantic import BaseModel

class GlobalConstants:
    CODE_TRANSFER_FILENAME =  "code.txt"
    ERROR = 'error'
    WARNING = 'warning'
    SUCCESS = 'success'
    
    ERROR_TYPE = 'eRROR'
    
    ATTR = 'attr'
    METHOD = 'method'
    PARAMETER = 'parameter'
    CLASS = 'class'
    EXPR = 'expr'
    
global_constants = GlobalConstants()