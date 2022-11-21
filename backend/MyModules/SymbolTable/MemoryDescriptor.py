from pydantic import BaseModel
from tabulate import tabulate

from Singleton import MySingleton

class MemoryDescriptorItem(BaseModel):
    address: int
    name: str
    typ: str
    scope: str
    size: int
    mem_base: int

class MemoryDescriptor(metaclass=MySingleton):
    def __init__(self):
        self.__items = []
        
    def add_item(self, item: MemoryDescriptorItem):
        self.__items.append(item)
    
    def get_item(self, address: int) -> MemoryDescriptorItem:
        for item in self.__items:
            if item.address == address:
                return item
        return None
    
    def get_item_by_name(self, name: str, scope: str) -> MemoryDescriptorItem:
        for item in self.__items:
            if item.name == name and item.scope == scope:
                return item
        return None
    
    def get_item_by_temp(self, temp: str) -> MemoryDescriptorItem:
        for item in self.__items:
            if item.name == temp:
                return item
        return None
    
    def __str__(self) -> str:
        mystr='Mi descriptor de memoria: \n'
        tab = tabulate(map(lambda x: x.dict(), self.__items), headers='keys')
        return mystr + tab
    
    def reset(self):
        self.__items = []
        
    