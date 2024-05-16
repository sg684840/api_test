import requests
import json
import csv
import pandas as pd


def extract_result_json(response_1 , response_2):
    data_1 = response_1['results'][0]
    data_2 = response_2['results'][0]
    gender_1 = data_1['gender']
    gender_2 = data_2['gender']
    name_1 = data_1['name']['first'] + " " + data_1['name']['last']
    name_2 = data_2['name']['first'] + " " + data_2['name']['last']
    street_1 = str(data_1['location']['street']['number']) +" "+ data_1['location']['street']['name']
    street_2 = str(data_2['location']['street']['number']) + " " + data_2['location']['street']['name']
    city_1 = data_1['location']['city']
    state_1 = data_1['location']['state']
    country_1 = data_1['location']['country']
    postcode_1 = data_1['location']['postcode']
    email_1 = data_1['email']

    city_2 = data_2['location']['city']
    state_2 = data_2['location']['state']
    country_2 = data_2['location']['country']
    postcode_2 = data_2['location']['postcode']
    email_2 = data_2['email']

    row = [gender_1,name_1,street_1,city_1,state_1,country_1,postcode_1,email_1,gender_2,name_2,street_2,
                        city_2,state_2,country_2,postcode_2,email_2]
    df = pd.DataFrame([row], columns=['gender_1','name_1','street_1','city_1','state_1','country_1','postcode_1','email_1',
                                                                                'gender_2','name_2','street_2','city_2','state_2','country_2','postcode_2','email_2'])
    df.to_csv('api_data.csv', index=False)


search_api_url = 'https://randomuser.me/api/'

for i in range(10):
    response_1 = requests.get(search_api_url)
    print(response_1.status_code)
    if response_1.status_code==200 :
        print(response_1.json())
        response_2 = requests.get(search_api_url)
        print(response_2.status_code)
        if response_2.status_code==200 :
            print(response_2.json())
            extract_result_json(response_1.json(), response_2.json())
        else :
            print("Response 2 error :", response_2.status_code)
    else :
        print("Response 1 error :", response_1.status_code)



#print(response_1.json()['results'][0]['gender'])