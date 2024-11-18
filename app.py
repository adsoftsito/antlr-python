from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser

origins = ["*"]

app = FastAPI(title = 'Hello Antlr')

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"]
)


class InputData(BaseModel):
    sentence:str=''

class OutputData(BaseModel):
    result:str=''

@app.post('/hello', response_model = OutputData)
def hello(data:InputData):

    input_text = data.sentence
    lexer = HelloLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)

    tree = parser.r()

    print(tree.toStringTree(recog=parser))    
    result = tree.toStringTree(recog=parser)    

    return {'result': result}
