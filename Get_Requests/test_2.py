import requests
import json
import pandas as pd

search_api_url = 'https://randomuser.me/api/'
response_1 = requests.get(search_api_url)
print(response_1.status_code)
if response_1.status_code==200 :
    print(response_1.json())
    response_2 = requests.get(search_api_url)
    print(response_2.status_code)
    if response_2.status_code==200 :
        print(response_2.json())
        if str(response_1.json())==str(response_2.json()) :
            print("True")
        else:
            print("False")
    else :
        print("Response 2 error :", response_2.status_code)
else :
    print("Response 1 error :", response_1.status_code)



