from utils.Utils import indx
from .Constants import constants
from tabulate import tabulate
from ConsoleMessages import MessagesDB
from pydantic import BaseModel
from Singleton import MySingleton
from Global import global_constants

class TableItem(BaseModel):
    lex: str
    token: int
    line: tuple[int, int]
    sem_kind: str
    byte_size: int = 0
    param_method: str | None = None
    typ: str | None = None
    param_num: int = 0
    mem_pos: int = 0
    mem_base: int = 0
    inherits: str | None = None

class Table(BaseModel):
    name: str
    items: list[TableItem] = []
        
        
class SymbolTable(metaclass=MySingleton):
    def __init__(self):
        self.tables = [Table(name=constants.string_literals.GLOBAL)]
        self.scopes = [0]
        self.msgs_db = MessagesDB()
        self.lets_counter = 0
        self.objects_counter = 0
        self.mem_counter = 0
        
        self.add_basic_types()
        
    
    def check_main(self) -> None:
        if self.check_main_existence():
            main_indx = indx(list(map(lambda x: x.lex, self.tables[0].items)), constants.string_literals.MAIN)
            main_line = self.tables[0].items[main_indx].line
            self.check_main_method(main_line)
        else:
            self.msgs_db.insert_error((0, 0), "No existe la clase main o está heredando de otra clase")
         
    def check_main_method(self, line: tuple[int, int]) -> None:
        main_table_indx = self.get_table_index(constants.string_literals.MAIN)
        main_m_indx = indx(list(map(lambda x: x.lex.lower(), self.tables[main_table_indx].items)), constants.string_literals.MAIN.lower())
        
        if main_m_indx < 0:
            self.msgs_db.insert_error(line, "El método main no ha sido declarado")
        else:
            main_m: TableItem = self.tables[main_table_indx].items[main_m_indx]
            
            if main_m.param_num > 0:
                self.msgs_db.insert_error(line, "El método main no debe tener parámetros")
            
            
    
    def check_main_existence(self) -> bool:
        return any(map(lambda x: x.lex == constants.string_literals.MAIN and x.inherits is None, self.tables[0].items))
    
    
    def add_int(self):
        int_item = TableItem(
            lex=global_constants.basic_types.INT,
            token=global_constants.token_types.TYPE,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.CLASS,
            byte_size=global_constants.byte_size.INT,
        )
        self.insert(int_item)
        
    def add_bool(self):
        bool_item = TableItem(
            lex=global_constants.basic_types.BOOL,
            token=global_constants.token_types.TYPE,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.CLASS,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.BOOL
        )
        self.insert(bool_item)
        
    def add_object(self):        
        object_i = TableItem(
            lex=global_constants.basic_types.OBJECT,
            token=global_constants.token_types.TYPE,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.CLASS,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.CLASS
        )
        self.insert(object_i)
        
        self.push_scope(global_constants.basic_types.OBJECT)
        
        abort_m_i = TableItem(
            lex=constants.object.ABORT,
            typ=global_constants.basic_types.OBJECT,
            token=global_constants.token_types.ID,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.METHOD,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.CLASS
        )
        
        self.insert(abort_m_i)
        
        type_name_m_i = TableItem(
            lex=constants.object.TYPE_NAME,
            typ=global_constants.basic_types.STRING,
            token=global_constants.token_types.ID,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.METHOD,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.STRING
        )
        
        self.insert(type_name_m_i)
        
        copy_m_i = TableItem(
            lex=constants.object.COPY,
            typ=global_constants.basic_types.OBJECT,
            token=global_constants.token_types.ID,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.METHOD,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.CLASS
        )
        
        self.insert(copy_m_i)
        
        self.pop_scope()
        
    def add_string(self):
        string_i = TableItem(
            lex=global_constants.basic_types.STRING,
            token=global_constants.token_types.TYPE,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.CLASS,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.STRING
        )
        self.insert(string_i)
        
        self.push_scope(global_constants.basic_types.STRING)
        
        length_m_i = TableItem(
            lex=constants.string.LENGTH,
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.INT,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.METHOD,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.INT
        )
        
        self.insert(length_m_i)
        
        concat_m_i = TableItem(
            lex=constants.string.CONCAT,
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.STRING,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.METHOD,
            param_method=constants.param_methods.VALUE,
            param_num=1,
            byte_size=global_constants.byte_size.STRING
        )
        
        self.insert(concat_m_i)
        
        self.push_scope(constants.string.CONCAT)
        
        concat_p_i = TableItem(
            lex = 's',
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.STRING,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.PARAMETER,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.STRING
        )
        
        self.insert(concat_p_i)
        
        self.pop_scope()
        
        substr_m_i = TableItem(
            lex=constants.string.SUBSTR,
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.STRING,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.METHOD,
            param_method=constants.param_methods.VALUE,
            param_num=2,
            byte_size=global_constants.byte_size.STRING
        )
        
        self.insert(substr_m_i)
        
        self.push_scope(constants.string.SUBSTR)
        
        substr_p_i_1 = TableItem(
            lex = 'i',
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.INT,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.PARAMETER,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.INT
        )
        
        self.insert(substr_p_i_1)
        
        substr_p_i_2 = TableItem(
            lex = 'l',
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.INT,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.PARAMETER,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.INT
        )
        
        self.insert(substr_p_i_2)
        
        self.pop_scope()
        
        self.pop_scope()
    
    def add_io(self):        
        io_i = TableItem(
            lex=global_constants.basic_types.IO,
            token=global_constants.token_types.TYPE,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.CLASS,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.CLASS + global_constants.byte_size.INT + global_constants.byte_size.STRING
        )
        self.insert(io_i)
        
        self.push_scope(global_constants.basic_types.IO)
        
        out_string_m_i = TableItem(
            lex=constants.io.OUT_STRING,
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.IO,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.METHOD,
            param_method=constants.param_methods.VALUE,
            param_num=1,
            byte_size=io_i.byte_size
        )
        
        self.insert(out_string_m_i)
        
        self.push_scope(constants.io.OUT_STRING)
        
        out_string_p_i = TableItem(
            lex='x',
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.STRING,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.PARAMETER,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.STRING
        )
        
        self.insert(out_string_p_i)
        
        self.pop_scope()
        
        
        out_int_m_i = TableItem(
            lex=constants.io.OUT_INT,
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.IO,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.METHOD,
            param_method=constants.param_methods.VALUE,
            param_num=1,
            byte_size=io_i.byte_size
        )
        
        self.insert(out_int_m_i)
        
        self.push_scope(constants.io.OUT_INT)
        
        out_int_p_i = TableItem(
            lex='x',
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.INT,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.PARAMETER,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.INT
        )
        
        self.insert(out_int_p_i)
        
        self.pop_scope()
        
        
        in_string_m_i = TableItem(
            lex=constants.io.IN_STRING,
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.STRING,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.METHOD,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.STRING
        )
        
        self.insert(in_string_m_i)
        
        in_int_m_i = TableItem(
            lex=constants.io.IN_INT,
            token=global_constants.token_types.ID,
            typ=global_constants.basic_types.INT,
            line=(0, 0),
            sem_kind=global_constants.sem_kinds.METHOD,
            param_method=constants.param_methods.VALUE,
            byte_size=global_constants.byte_size.INT
        )
        
        self.insert(in_int_m_i)
                
        self.pop_scope()
        
    
    def add_basic_types(self):
        self.add_int()
        self.add_bool()
        self.add_object()
        self.add_string()
        self.add_io()

    def push_scope(self, scope: str) -> None:
        self.tables.append(Table(name=scope))
        self.scopes.append(len(self.tables) - 1)

    def pop_scope(self) -> None:
        self.scopes.pop()
        
    def enter_scope(self, scope: str) -> None:
        self.scopes.append(self.get_table_index(scope))
        
    def exit_scope(self) -> None:
        self.scopes.pop()
        
    def get_table_index(self, scope: str) -> int:
        for i, table in enumerate(self.tables):
            if table.name == scope:
                return i
        
        return -1
    
    
    def insert(self, item: TableItem) -> bool:
        if (item.lex, item.sem_kind) in map(lambda x: (x.lex, x.sem_kind), self.tables[self.actual_scope].items):
            self.msgs_db.insert_error(item.line, global_constants.sem_kinds.KIND_TABLE_ERROR[item.sem_kind] + ' ' + item.lex + ' ya declarada ')
            return False
        else:
            self.tables[self.actual_scope].items.append(item)
            return True


    def get(self, name):
        for scope in reversed(self.scopes):
            for row in self.tables[scope].items:
                if row.lex == name:
                    return row
                
        return None
    
    def exists(self, name):
        for scope in reversed(self.scopes):
            for row in self.tables[scope].items:
                if row.lex == name:
                    return True
                
        return False
    
    def get_from_table(self, index: int, name: str):
        for row in self.tables[index].items:
            if row.lex == name:
                return row
                
        return None
    
    def exists_in_table(self, index: int, name):
        for row in self.tables[index].items:
            if row.lex == name:
                return True
                
        return False
    
    def add_byte_size(self, index: int, name: str, size: int):
        for row in self.tables[index].items:
            if row.lex == name:
                row.byte_size += size
                return True
                
        return False
    
    def add_class_size(self, name: str ,size: int):
        self.get_from_table(0, name).byte_size += size
    
    def get_byte_size(self, name: str):
        table_item = self.get_from_table(0, name)
        
        return table_item.byte_size
    
    def inherits_from(self, child: str, parent: str):
        if child == parent:
            return False
        
        elem: TableItem = self.get_from_table(0, child)
        
        return parent == elem.inherits

    def set_mem_pos(self, name: str, pos: int):
        for index, symbol in enumerate(self.tables[self.actual_scope].items):
            if symbol.lex == name:
                self.tables[self.actual_scope].items[index].mem_pos = pos
                return True
        return False
    
    def allocate_mem_pos(self, mem_size: int) -> int:
        self.mem_counter += mem_size
        return self.mem_counter - mem_size
        
    def update_mem_position(self, index: int):
        for elem in self.tables[index].items:
            index = self.get_table_index(elem.lex)
            
            if index != -1:
                self.update_mem_position(index)
                
            if elem.sem_kind == global_constants.sem_kinds.ATTR or elem.sem_kind == global_constants.sem_kinds.PARAMETER:
                elem.mem_pos = self.allocate_mem_pos(elem.byte_size)
    
    @property
    def actual_scope(self):
        return self.scopes[-1]
    
    @property
    def actual_scope_name(self):
        return self.tables[self.actual_scope].name
    
    @property
    def symbol_table(self):
        return self.tables
    
    @symbol_table.deleter
    def symbol_table(self):
        self.tables = [Table(name=constants.string_literals.GLOBAL)]
        self.scopes = [0]
        self.lets_counter = 0
        
        self.add_basic_types()

    def mem_reset(self):
        self.mem_counter = 0
    
    def __str__(self):
        mystr = ''
        for table in self.tables:
            tab = tabulate(map(lambda x: x.dict(), table.items), headers='keys')
            mystr+= f'\n\n{table.name}:\n{tab}'
            
        return mystr
    
    