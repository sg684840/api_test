import requests
import json
import pandas as pd

df = pd.read_csv("C:/Users/SOUMYA/PycharmProjects/api_test/Get_Requests/Input_File/get_request.csv")
#print(df.id)
for i in df.id:
    print("value:",i)
    search_api_url = 'https://reqres.in/api/users/' + str(i)
    response = requests.get(search_api_url)
    print(response.status_code)
    print(response.json())