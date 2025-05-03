# Example of service usage
import requests

# firstly compose up your service
url = "http://localhost:8081/embed"
data = {"chunks": ["lol", "kek", "cheburek"]}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.json())
