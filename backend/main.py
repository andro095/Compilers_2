# Librerias de Python
import sys
import os

# Librerias de terceros
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from fastapi import FastAPI
from pydantic import BaseModel

sys.path.append('./MyModules')

# Librerias Propias
from YAPL import YaplLexer, YaplParser, YaplListener, YaplErrorListener
from ConsoleMessages import MessagesDB
from Constants import global_constants

app = FastAPI()
msgs_db = MessagesDB()


class Code(BaseModel):
    code: str
    

@app.post("/upload")
def upload_file():
    pass

@app.post("/execute")
def execute_code(code: Code):
    with open(global_constants.CODE_TRANSFER_FILENAME, 'w') as f:
        f.write(code.code)
        f.close()
        
    process_code()
    messages = msgs_db.messages
    
    del msgs_db.messages
        
    return { 'messages': messages }

def process_code():
    f_stream = FileStream(global_constants.CODE_TRANSFER_FILENAME)
    
    os.remove(global_constants.CODE_TRANSFER_FILENAME)
    
    lexer = YaplLexer(f_stream)
    
    stream = CommonTokenStream(lexer)
    parser = YaplParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(YaplErrorListener.INSTANCE)
    tree = parser.program()
    printer = YaplListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    






