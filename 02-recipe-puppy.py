import requests
import json

ilosc = input('Podaj ilosc faktow, kóre chcesz otrzymać: ')


response = requests.get(f'https://meowfacts.herokuapp.com/?count={ilosc}')


if (response.status_code != requests.codes.ok):
    print('coś poszło nie tak')
else:
    print(json.dumps(response.json(), indent=4))
