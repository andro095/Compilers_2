class PhaseError:
    LEXIC = 'léxico'
    SINTACTIC = 'sintáctico'
    SEMANTIC = 'semántico'

class TokenTypes:
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


class ByteSize:
    INT = 4
    STRING = 50
    BOOL = 1
    CLASS = 100

class OperatorConstants:
    token_types = TokenTypes()
    
    op_dict = {
        token_types.ADD: '+',
        token_types.SUB: '-',
        token_types.MULTIPLY: '*',
        token_types.DIVIDE: '/',
        token_types.LESS_THAN: '<',
        token_types.LESS_EQUAL: '<=',
        token_types.EQUAL: '==',
    }
class SemanticKinds:
    CLASS = 'class'
    ATTR = 'attr'
    METHOD = 'method'
    PARAMETER = 'parameter'
    EXPR = 'expr'
    OBJ = 'obj'
    
    KIND_TABLE_ERROR = {
        ATTR: 'Variable',
        METHOD: 'Método',
        PARAMETER: 'Parámetro',
        CLASS: 'Clase'
    }

class ResultsTypes: 
    ERROR_TYPE = 'eRROR'
    NO_TYPE = 'noType'
    CHECK_TYPE = 'checkType'

class StringConstants:
    LET = 'let'
    IN = 'in'
    TYPE_DELIMITER = ':'
    FALSE = 'false'
    TRUE = 'true'
    
class BaseMemory:
    HEAP = 0
    STACK = 1

class GlobalConstants:      
    basic_types = BasicTypes()    
    BASIC_TYPES = [basic_types.INT, basic_types.BOOL, basic_types.STRING]
    
    base_memory = BaseMemory()
    byte_size = ByteSize()
    phase_error = PhaseError()
    results_types = ResultsTypes()
    sem_kinds = SemanticKinds()
    string_cons = StringConstants()
    op_dict = OperatorConstants().op_dict
    token_types = TokenTypes()
    
    LOGIC_OPERATORS = [op_dict[token_types.LESS_THAN], op_dict[token_types.LESS_EQUAL], op_dict[token_types.EQUAL]]
    MEM_SEM_KINDS = [sem_kinds.ATTR, sem_kinds.PARAMETER, sem_kinds.OBJ]
    BASIC_TOKENS = [token_types.INTEGER, token_types.STRING, token_types.TRUE, token_types.FALSE]
    COND_TOKENS = [token_types.IF, token_types.WHILE]
    
global_constants = GlobalConstants()