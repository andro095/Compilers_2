from .Message import Message, make_message
from Global import global_constants
from Singleton import MySingleton

class MessagesDB(metaclass=MySingleton):
    def __init__(self):
        self.__messages: list[Message] = []
        
    def insert_message(self, msg: str, color: str | None = None, type: str | None = None) -> None:
        self.__messages.append(make_message(msg, color, type))
        
    def insert_error(self, line: tuple, msg: str) -> None:
        msg = f'Error en la línea {line[0]}:{line[1]}\n{msg}'
        self.__messages.append(make_message(msg, type=global_constants.ERROR))
    
    def insert_warning(self, line: tuple, msg: str) -> None:
        msg = f'Advertencia en la línea {line[0]}:{line[1]}\n{msg}'
        self.__messages.append(make_message(msg, type=global_constants.WARNING))
        
    def insert_success(self):
        msg = 'Código ejecutado correctamente'
        self.__messages.append(make_message(msg, type=global_constants.SUCCESS))
    
    @property    
    def messages(self) -> list[Message]:
        return self.__messages
    
    @messages.deleter
    def messages(self) -> None:
        self.__messages = []