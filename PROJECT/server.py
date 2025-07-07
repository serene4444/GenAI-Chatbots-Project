"""
Created on 07/06/2025

@author: Serene Plummer
"""

from llama_index.core import VectorScore, SimpleDirectoryReader, StorageContext

from dotenv import load_dotenv
import os

from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

load_dotenv()

api_key= os.get.env("OPENAI_API_KEY")

if api_key:
    print("API key: " + api_key[0:6])
else:
    print("API key not found")

storage_content = StorageContent.from_defaults(persist_dir = "ml_index")

index = load_index_from_storage(storage_content)

engine = index.as_query