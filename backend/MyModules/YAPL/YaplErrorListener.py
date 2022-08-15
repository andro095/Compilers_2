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
        msg = msg.replace(' expecting ', ', se esperaba uno de los siguientes valores: ')
        message = 'Error de sintaxis en la linea ' + str(line) + ':' + str(column) + '\n\t' + msg
        self.msgs_db.insert_message(message, type='error')

YaplErrorListener.INSTANCE = YaplErrorListener()