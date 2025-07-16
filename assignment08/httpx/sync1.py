import requests

requests = requests.get("https://httpbin.org/delay/3")
print(f"Status code: {requests.status_code}")