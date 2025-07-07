"""
Created on 07/05/2025

@author: Serene Plummer
"""

from dotenv import load_dotenv
import os

load_dotenv()

api_key =os.getenv("OPENAI_API_KEY")

if api_key:
    print("API key: " + api_key[0:6])
else:
    print("API key not found")

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(completion.choices[0].message.content)