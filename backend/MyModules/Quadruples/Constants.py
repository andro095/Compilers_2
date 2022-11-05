class Operators:
    arimetic_opeators = {
        '+': 'add',
        '-': 'sub',
        '*': 'mult',
        '/': 'div',
    }


class Regrexes:
    INTEGER = r"^[0-9]+$"
    STRING = r"\"\w*?\""
    MEM_POS = r"[a-zA-Z]+[_][a-z]\[[0-9]+\]"
    TEMPS = r"[t][0-9]+"

class Constants:
    operators = Operators()
    regrexes = Regrexes()
    
constants = Constants()