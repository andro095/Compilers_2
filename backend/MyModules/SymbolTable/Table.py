from .Constants import constants
from utils import error
from tabulate import tabulate
from ConsoleMessages import MessagesDB


# TODO: Remplazar los errores de consola por errores de la clase MessagesDB
class SymbolTable:
    def __init__(self):
        self.table = []
        self.scopes = [constants.GLOBAL]
        self.msgs_db = MessagesDB()

    def push_scope(self, scope):
        self.scopes.append(scope)

    def pop_scope(self):
        self.scopes.pop()

    def insert(self, name, typ, kind, scope, line, value=None):
        scope_variables = filter(lambda x: x['scope'] == scope, self.table)
        if (name, kind) in map(lambda x: (x['name'], x['kind']), scope_variables):
            error(constants.KIND_TABLE_ERROR[kind] + ' ' + name + ' ya declarada ', line)

        self.table.append({'name': name, 'type': typ, 'kind': kind, 'scope': scope, 'line': line, 'value': value})

    def get(self, name, line,scope=None):
        if scope is None:
            scope = self.get_scope()

        scope_variables = filter(lambda x: x['scope'] == scope, self.table)
        for variable in scope_variables:
            if variable['name'] == name:
                return variable

        error('Variable ' + name + ' no declarada', line)

    def set(self, name, line, value):
        for scope in reversed(self.scopes):
            for row in self.table:
                if row['name'] == name and row['scope'] == scope:
                    row['value'] = value
                    return

        error('Variable ' + name + ' no declarada', line)

    def get_scope(self):
        return self.scopes[-1]

    def __str__(self):
        table = map(lambda x: x.values(), self.table)
        return tabulate(table, headers=['name', 'type', 'kind', 'scope', 'line', 'value'])
