from pydantic import BaseModel
from antlr4 import *
from YAPL import YaplLexer, YaplParser, YaplListener, YaplVisitor, YaplErrorListener
import os
from fastapi import FastAPI

app = FastAPI()

class Code(BaseModel):
    code: str
    

@app.post("/upload")
def upload_file():
    pass

@app.post("/execute")
def execute_code(code: Code):
    with open('code.txt', 'w') as f:
        f.write(code.code)
        f.close()
        
    process_code()
        
    return {"code": code.code}

def process_code():
    input = FileStream('code.txt')
    
    os.remove('code.txt')
    
    lexer = YaplLexer(input)
    
    stream = CommonTokenStream(lexer)
    parser = YaplParser(stream)
    parser.addErrorListener(YaplErrorListener())
    tree = parser.program()
    printer = YaplListener()
    walker = ParseTreeWalker()
    res = walker.walk(printer, tree)






