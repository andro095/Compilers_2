from antlr4 import *
from YAPL import YaplLexer, YaplParser, YaplListener, YaplVisitor, YaplErrorListener
import sys

def read_types(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        tokens = list(filter(lambda token: "'" not in token, lines))
        tokens = list(map(lambda token: token.split('=')[0], tokens))

        return tokens

def main(file_name: str, token_types: list):
    input = FileStream(file_name)

    lexer = YaplLexer(input)
    # lexerParse = YaplLexer(input)
    #
    # token = lexer.nextToken()
    #
    # print('Tokens reconocidos:')
    #
    # while token.type != token.EOF:
    #     print('\t' + str(token_types[token.type - 1]) + ': ' + str(token.text) + ', linea: ' + str(token.line))
    #     token = lexer.nextToken()

    stream = CommonTokenStream(lexer)
    parser = YaplParser(stream)
    parser.addErrorListener(YaplErrorListener())
    tree = parser.program()
    printer = YaplListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)



if __name__ == '__main__':
    posible_tokens = read_types('YAPL/Yapl.tokens')

    file_name: str = 'examples/cons.yapl'
    # # file_name: str = sys.argv[1] if len(sys.argv) > 1 else input("Ingresa el nombre del archivo: ")
    main(file_name, posible_tokens)
