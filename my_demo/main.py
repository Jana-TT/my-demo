from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"PP": "Poopie"}


@app.get("/greeting/{greetings}")
async def read_item(greetings: str):
    return {"Wowie,": greetings} 

