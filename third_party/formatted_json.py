"""
Dump json-objects in a formatted way.
"""
import json
import requests


def sample_request(url: str):
    resp = requests.get(url)

    return resp.json()


response = sample_request("https://jsonplaceholder.typicode.com/todos/1")
print(json.dumps(response, indent=4))
input()
