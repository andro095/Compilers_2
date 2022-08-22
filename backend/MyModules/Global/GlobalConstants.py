from pydantic import BaseModel

class GlobalConstants:
    CODE_TRANSFER_FILENAME =  "code.txt"
    ERROR = 'error'
    WARNING = 'warning'
    SUCCESS = 'success'
    
class Error(BaseModel):
    msg: str
    
global_constants = GlobalConstants()