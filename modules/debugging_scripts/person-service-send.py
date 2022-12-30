import requests

API_URL = "http://localhost:30010/api"

# # should return the default route"s output
result = requests.get(API_URL + "/persons/1")
print(result.json())


# # should return the demo path example
# result = requests.post(API_URL + "/persons/1", json={"key": "value"}, headers={"header_demo": "myHeader"})
# print(result.json())
