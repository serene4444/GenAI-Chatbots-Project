"""
Created on 07/06/2025

@author: Serene Plummer
"""

import requests

#Define the URL
url = "http://127.0.0.1:8000/sum"

#Define the numbers to be sent
data = {
    "number1": 5,
    "number2": 7
}

#Send a POST request to the URL with the numbers
try:
    response = requests.post(url, json=data)
    if response.status_code == 200:
        #If successful, print the response
        print("Response:", response.json())
    else:
        #If not successful, print the error
        print("Error:", response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print("Connection error:", e)
