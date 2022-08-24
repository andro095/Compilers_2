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
    answer = YaplVisitor().visit(tree)
    print(answer)
    answer2 = YaplSysTypeVisitor().visit(tree)
    print(answer2)

    messages = msgs_db.messages
    
    del sym_table.symbol_table
    del msgs_db.messages
        
    return { 'messages': messages }







