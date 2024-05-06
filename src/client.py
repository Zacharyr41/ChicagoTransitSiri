import requests
import json

URL = "http://127.0.0.1"
PORT = "8080"
ENDPOINT = "/chat"

def call_sanic():
    # full_uri = URL + ":" + PORT + ENDPOINT
    full_uri = "https://01a4-128-135-204-82.ngrok-free.app/chat"
    data = {"query" : "When will the four bus heading north arrive at 57th street and cottage grove"}
    response = requests.post(full_uri, data=json.dumps(data))
    return response

if __name__ == "__main__":
    print("Response: ", call_sanic().text)