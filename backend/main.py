    # Librerias de Python
import imp
import sys
import os
from tkinter.tix import Tree

# Librerias de terceros
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, Token
from antlr4.tree.Trees import Trees
from fastapi import FastAPI
from pydantic import BaseModel
import svgling

sys.path.append('./MyModules')

# Librerias Propias
from YAPL import YaplLexer, YaplParser, YaplErrorListener, YaplVisitor, YaplSysTypeVisitor
from ConsoleMessages import MessagesDB
from SymbolTable import SymbolTable
from Global import global_constants

app = FastAPI()
msgs_db = MessagesDB()
sym_table = SymbolTable()


class Code(BaseModel):
    code: str
    

@app.post("/upload")
def upload_file():
    """_summary_: Función para controlar un error del frontend.
    """    
    pass

@app.post("/execute")
def execute_code(code: Code) -> dict:
    """Función para ejecutar el código de YAPL.

    Argumentos:
        code (Code): Código de YAPL.

    Retorna:
        dict: Diccionario con los mensajes de salida.
    """            
    
    i_stream = InputStream(code.code)
    
    lexer = YaplLexer(i_stream)
    haslexer_errors = False
    
    actual_token = lexer.nextToken()
    while actual_token.type != Token.EOF:
        if actual_token.type == lexer.ERR_TOKEN:
            line = (actual_token.line, actual_token.column)
            msgs_db.insert_error(line, f'Caracter no reconocido: {actual_token.text}', 'léxico')
            haslexer_errors = True
        actual_token = lexer.nextToken()
            
    if not haslexer_errors:
        msgs_db.insert_success('El análisis léxico fue exitoso.')
    
    lexer.reset()
    
    stream = CommonTokenStream(lexer)
    parser = YaplParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(YaplErrorListener.INSTANCE)    
    tree = parser.program()
    if not msgs_db.error_flag:       
        msgs_db.insert_success('El  sintáctico fue exitoso.')
    del msgs_db.error_flag
    YaplVisitor().visit(tree)
    if not msgs_db.error_flag:
        msgs_db.insert_success('La inserción de tipos fue exitosa.')
    answer2 = YaplSysTypeVisitor().visit(tree)
    print(answer2)
    if answer2 == global_constants.CHECK_TYPE:
        msgs_db.insert_success("El análisis semantico fue exitoso.")
                

    messages = msgs_db.messages
    
    del sym_table.symbol_table
    del msgs_db.messages
    del msgs_db.error_flag
        
    return { 'messages': messages }







