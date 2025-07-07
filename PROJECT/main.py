"""
Created on 07/06/2025

@author: Serene Plummer
"""
import uvicorn
from fastapi import FastAPI

#Create an instance of FastAPI class
app = FastAPI()

#define a route to handle GET requests to the root URL
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)