from antlr4 import *
from YAPL import YaplLexer, YaplParser, YaplListener, YaplVisitor, YaplErrorListener
import sys


def main(file_name: str):
    input = FileStream(file_name)

    lexer = YaplLexer(input)

    # token = lexer.nextToken()
    #
    # print('Tokens reconocidos:')
    #
    # while token.type != token.EOF:
    #     print('\t' + str(token_types[token.type - 1]) + ': ' + str(token.text) + ', linea: ' + str(token.line))
    #     token = lexer.nextToken()
    #
    # lexer = YaplLexer(input)

    stream = CommonTokenStream(lexer)
    parser = YaplParser(stream)
    parser.addErrorListener(YaplErrorListener())
    tree = parser.program()
    printer = YaplListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)



if __name__ == '__main__':
    file_name: str = 'examples/cons.yapl'
    # # file_name: str = sys.argv[1] if len(sys.argv) > 1 else input("Ingresa el nombre del archivo: ")
    main(file_name)
