import sys


class YaplErrorListener(object):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print('Error de sintaxis en la linea ' + str(line) + ': ' + msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print('Hola')

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print('Hola 2')

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print('Hola 3')
