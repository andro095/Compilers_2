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
from YAPL import YaplLexer, YaplParser, YaplErrorListener, YaplVisitor, YaplSysTypeVisitor, YaplInterCodeVisitor
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
            
    if not haslexer_errors and not msgs_db.has_lexical_errors:
        msgs_db.insert_success('El análisis léxico fue exitoso.')
    
    lexer.reset()
    
    stream = CommonTokenStream(lexer)
    parser = YaplParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(YaplErrorListener.INSTANCE)    
    tree = parser.program()
    has_sintactic_errors = False
    has_semantic_errors = False
    has_insertion_errors = False
    if not msgs_db.error_flag and not msgs_db.has_sintactic_errors:       
        msgs_db.insert_success('El  sintáctico fue exitoso.')
    else:
        has_sintactic_errors = True
    del msgs_db.error_flag
    YaplVisitor().visit(tree)
    if not msgs_db.error_flag:
        msgs_db.insert_success('La inserción de tipos fue exitosa.')
    else:
        has_insertion_errors = True
    try:
        answer2 = YaplSysTypeVisitor().visit(tree)
        if answer2 == global_constants.results_types.CHECK_TYPE and not msgs_db.has_semantic_errors:
            msgs_db.insert_success("El análisis semantico fue exitoso.")
        else:
            has_semantic_errors = True
    except:
        pass
    
    intercode = ''
    
    has_errors = has_sintactic_errors or has_semantic_errors or has_insertion_errors or haslexer_errors
    has_errors2 = msgs_db.has_lexical_errors or msgs_db.has_sintactic_errors or msgs_db.has_semantic_errors
    
    if not has_errors and not has_errors2:
        intercode = YaplInterCodeVisitor().visit(tree)

    messages = msgs_db.messages
    
    del sym_table.symbol_table
    sym_table.mem_reset()
    del msgs_db.messages
    del msgs_db.error_flag
        
    return { 'messages': messages, 'intercode': intercode }







