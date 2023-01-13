import requests
import json


search_api_url = 'https://reqres.in/api/users/2'
response = requests.get(search_api_url)
print(response.status_code)
print(response.json())