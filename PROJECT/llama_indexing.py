"""
Created on 07/06/2025

@author: Serene Plummer
"""
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

from dotenv import load_dotenv
import os
import sys

load_dotenv()

api_key =os.getenv("OPENAI_API_KEY")

if api_key:
    print("API key: " + api_key[0:6])
else:
    print("API key not found")

try:
    documents = SimpleDirectoryReader("pdf").load_data()
    if not documents:
        print("No documents found in the specified directory.")
        sys.exit(1)
except Exception as e:
    print(f"Error loading documents: {e}")
    sys.exit(1)
    
index = VectorStoreIndex.from_documents(documents)
engine = index.as_query_engine()

result = engine.query("What are the strengths of R over Python?")
print(result)

index.storage_context.persist("ml_index")
