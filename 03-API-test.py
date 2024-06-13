import requests
import json

response = requests.get('https://randomuser.me/api')
print(response.status_code)

gender = response.json()['results'][0]['gender']
print(gender)

first_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']
print(first_name,last_name)

age = response.json()['results'][0]['dob']['age']
print(f'AGE: {age}')