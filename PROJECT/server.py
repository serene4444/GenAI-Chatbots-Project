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

