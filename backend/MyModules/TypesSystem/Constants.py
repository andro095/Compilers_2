
class Constants:
    INDIVIDUAL_RULES = './TypesSystem/Rules/individual_rules.json'
    COMPLEX_RULES = './TypesSystem/Rules/complex_rules.json'
    EXPR = 'expr'
    LET = 'let'
    IN = 'in'

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

class BasicTypes:
    INT = 'Int'
    BOOL = 'Bool'
    OBJECT = 'Object'
    STRING = 'String'
    IO = 'IO'
    SELF_TYPE = 'SELF_TYPE'
    
basic_types = BasicTypes()

typs = TypesConstants()
    

types_sys_constants = Constants()