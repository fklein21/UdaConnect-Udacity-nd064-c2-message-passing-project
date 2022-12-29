import requests

API_URL = "http://localhost:30010/person"

# should return the default route"s output
result = requests.get(API_URL)
if result.status_code == 200:
    print(result.json())
