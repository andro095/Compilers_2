


import io
from typing import Literal


class ObjectConstants:
    ABORT = "abort"
    TYPE_NAME = 'type_name' 
    COPY = 'copy'
    
class StringConstants:
    LENGTH = 'length'
    CONCAT = 'concat'
    SUBSTR = 'substr'
    
class IOConstants:
    OUT_STRING = 'out_string'
    OUT_INT = 'out_int'
    IN_STRING = 'in_string'
    IN_INT = 'in_int'
    
class BasicTypes:
    INT = 'Int'
    BOOL = 'Bool'
    OBJECT = 'Object'
    STRING = 'String'
    IO = 'IO'
    SELF_TYPE = 'SELF_TYPE'

class Constants:
    GLOBAL = 'Global'
    
    MAIN = 'Main'

    ATTR = 'attr'
    METHOD = 'method'
    PARAMETER = 'parameter'
    CLASS = 'class'

    SELF_TYPE = 'SELF_TYPE'
    SELF = 'self'

    KIND_TABLE_ERROR = {
        ATTR: 'Variable',
        METHOD: 'Método',
        PARAMETER: 'Parámetro',
        CLASS: 'Clase'
    }
    
    REF = 'ref'
    VALUE = 'value'
    
    ARROW_ASIGN = '<-'
    TYPE_DELIMITER = ':'
    CROUND = ')'
    COMMA = ','
    INHERITS = ['inherits', 'INHERITS']
    
    types = BasicTypes()    
    
    BASIC_TYPES = [types.INT, types.BOOL, types.STRING]
    
    object = ObjectConstants()
    string = StringConstants()
    io = IOConstants()
    
    


class TypesConstants:
    CLASS = 1
    ELSE = 2
    FI = 3
    IF = 4
    IN = 5
    INHERITS = 6
    ISVOID = 7
    LOOP = 8
    POOL = 9
    THEN = 10
    WHILE = 11
    NEW = 12
    NOT = 13
    LET = 14
    FALSE = 15
    TRUE = 16
    SEMICOLON = 17
    LCURLY = 18
    RCURLY = 19
    LSQUARE = 20
    RSQUARE = 21
    LROUND = 22
    RROUND = 23
    COMMA = 24
    POINT = 25
    QUOTES = 26
    APOSTROPHE = 27
    ADD = 28
    SUB = 29
    MULTIPLY = 30
    DIVIDE = 31
    INT_NOT = 32
    COLON = 33
    ASIGN = 34
    ARROBA = 35
    LESS_THAN = 36
    LESS_EQUAL = 37
    EQUAL = 38
    LINE_COMMENT = 39
    COMMENT = 40
    INTEGER = 41
    STRING = 42
    TYPE = 43
    ID = 44
    WS = 45


types = TypesConstants()

constants = Constants()
