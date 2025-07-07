"""
Created on 07/06/2025

@author: Serene Plummer
"""
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

class Item(BaseModel):
    number1: float
    number2: float

#Create an instance of FastAPI class
app = FastAPI()

#define a route to handle GET requests to the root URL
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.post("/sum")
async def sum(item: Item):
    return {"result": item.number1 + item.number2}

if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)