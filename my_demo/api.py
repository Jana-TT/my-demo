import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Message": "Hello Poopie World!"}

@app.get("/message")
async def read_message(parameter: str):
    return {"Message": parameter}

@app.get("/luckyno")
async def read_lucky_num(number: int):
    return {"Your lucky number": number}

