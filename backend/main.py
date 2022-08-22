# Librerias de Python
import sys
import os

# Librerias de terceros
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from fastapi import FastAPI
from pydantic import BaseModel

sys.path.append('./MyModules')

# Librerias Propias
from YAPL import YaplLexer, YaplParser, YaplListener, YaplErrorListener
from ConsoleMessages import MessagesDB
from Global import global_constants

app = FastAPI()
msgs_db = MessagesDB()


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
    printer = YaplListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    messages = msgs_db.messages
    
    del msgs_db.messages
        
    return { 'messages': messages }







