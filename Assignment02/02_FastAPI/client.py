import requests

response = requests.get('http://127.0.0.1:8000/');
print(f"StatusCode: {response.status_code}, ResponseContent:{response.json()}")