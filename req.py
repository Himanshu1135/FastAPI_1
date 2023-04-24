import requests
import json

url = "http://127.0.0.1:8000/predict"

inp_data = {
    'variance': 0.0, 
    'skewness': 0.0, 
    'curtosis': 0.7, 
    'entropy': 0.1
}

inpt_json = json.dumps(inp_data)

resp = requests.post(url,data=inpt_json)
print(resp.text)
