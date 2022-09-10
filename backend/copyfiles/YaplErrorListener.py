import imp
import sys
from antlr4.error.ErrorListener import ErrorListener

from ConsoleMessages import MessagesDB


class YaplErrorListener(ErrorListener):
    INSTANCE = None
    
    def __init__(self):
        self.msgs_db = MessagesDB()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = msg.replace('mismatched input ', 'Entrada no válida ')
        msg = msg.replace('extraneous input ', 'Entrada no esperada ')
        msg = msg.replace(' expecting ', ', se esperaba uno de los siguientes valores: ')
        message = msg + '.'
        self.msgs_db.insert_error((line, column), message)

YaplErrorListener.INSTANCE = YaplErrorListener()