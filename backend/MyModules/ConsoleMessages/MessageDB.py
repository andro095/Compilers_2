from .Message import Message, make_message
from Global import global_constants
from Singleton import MySingleton

class MessagesDB(metaclass=MySingleton):
    def __init__(self):
        self.__messages: list[Message] = []
        self.__error_flag: bool = False
        
    def activate_error_flag(self):
        self.error_flag = True
        
    def insert_message(self, msg: str, color: str | None = None, type: str | None = None) -> None:
        self.__messages.append(make_message(msg, color, type))
        
    def insert_error(self, line: tuple, msg: str, type='semántico') -> None:
        self.activate_error_flag()
        msg = f'Error de tipo {type} en la línea {line[0]}:{line[1]}\n\t{msg}'
        self.__messages.append(make_message(msg, type=global_constants.ERROR))
    
    def insert_warning(self, line: tuple, msg: str) -> None:
        msg = f'Advertencia en la línea {line[0]}:{line[1]}\n{msg}'
        self.__messages.append(make_message(msg, type=global_constants.WARNING))
        
    def insert_success(self, msg: str) -> None:
        self.__messages.append(make_message(msg, type=global_constants.SUCCESS))
    
    @property    
    def messages(self) -> list[Message]:
        return self.__messages
    
    @messages.deleter
    def messages(self) -> None:
        self.__messages = []
        
    @property
    def error_flag(self) -> bool:
        return self.__error_flag
    
    @error_flag.setter
    def error_flag(self, value: bool) -> None:
        self.__error_flag = value
    
    @error_flag.deleter
    def error_flag(self) -> None:
        self.__error_flag = False