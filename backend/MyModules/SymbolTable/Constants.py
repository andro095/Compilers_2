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
    
class ParamMethods:
    REF = 'ref'
    VALUE = 'value'
    
class StringLiterals:
    CROUND = ')'
    COMMA = ','
    INHERITS = ['inherits', 'INHERITS']
    GLOBAL = 'Global'
    MAIN = 'Main'
    SELF = 'self'

class Constants:
    io = IOConstants()
    param_methods = ParamMethods()
    object = ObjectConstants()
    string = StringConstants()
    string_literals = StringLiterals()
    

constants = Constants()
