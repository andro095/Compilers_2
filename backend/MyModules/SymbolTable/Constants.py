


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
    EXPR = 'expr'

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
    LET = 'let'
    
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
    VOID = 17
    SEMICOLON = 18
    LCURLY = 19
    RCURLY = 20
    LSQUARE = 21
    RSQUARE = 22
    LROUND = 23
    RROUND = 24
    COMMA = 25
    POINT = 26
    QUOTES = 27
    APOSTROPHE = 28
    ADD = 29
    SUB = 30
    MULTIPLY = 31
    DIVIDE = 32
    INT_NOT = 33
    COLON = 34
    ASIGN = 35
    ARROBA = 36
    LESS_THAN = 37
    LESS_EQUAL = 38
    EQUAL = 39
    LINE_COMMENT = 40
    COMMENT = 41
    INTEGER = 42
    STRING = 43
    TYPE = 44
    ID = 45
    WS = 46
    ERR_TOKEN = 47


types = TypesConstants()

constants = Constants()
