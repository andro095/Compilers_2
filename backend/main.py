    # Librerias de Python
import sys
import os

# Librerias de terceros
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from fastapi import FastAPI
from pydantic import BaseModel

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
    
    stream = CommonTokenStream(lexer)
    parser = YaplParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(YaplErrorListener.INSTANCE)    
    tree = parser.program()
    if not msgs_db.error_flag:
        msgs_db.insert_success('Analizador léxico y sintáctico exitoso.')
        answer = YaplVisitor().visit(tree)
        if answer == global_constants.CHECK_TYPE:
            msgs_db.insert_success('La inserción de tipos fue exitosa.')
        if not msgs_db.error_flag:
            answer2 = YaplSysTypeVisitor().visit(tree)
            if answer2 == global_constants.CHECK_TYPE:
                msgs_db.insert_success("El análisis de tipos fue exitoso.")
                

    messages = msgs_db.messages
    
    del sym_table.symbol_table
    del msgs_db.messages
    del msgs_db.error_flag
        
    return { 'messages': messages }







