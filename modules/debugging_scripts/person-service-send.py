import requests

API_URL = "http://localhost:30010/api"


# Script for sending sample requests to the persons endpoint
# For debugging purposes


# # should return the default route"s output
result = requests.get(API_URL + "/persons/5")
print(result.json())
