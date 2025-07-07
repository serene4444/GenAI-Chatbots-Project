"""
Created on 07/06/2025

@author: Serene Plummer
"""

from llama_index.core import VectorScore, SimpleDirectoryReader, StorageContext
from llama_index.core import load_index_from_storage

from dotenv import load_dotenv
import os

from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

class Item(BaseModel):
    question: str


load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

if api_key:
    print("API key: " + api_key[0:6])
else:
    print("API key not found")

storage_content = StorageContext.from_defaults(persist_dir = "ml_index")

index = load_index_from_storage(storage_content)

engine = index.as_query_engine()

app = FastAPI()
@app.post("/")
async def query(item: Item):
    result = engine.query(item.question)
    return{"response": str(result)}

if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)