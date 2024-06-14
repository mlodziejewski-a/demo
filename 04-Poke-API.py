import requests


pokemon = input('Wprowadz nazwe pokemona: ')

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
print(response.status_code)
print(response.json().keys())


height = response.json()['height']
poke_type = response.json()['types'][0]['type']['name']
location_enc = response.json()['location_area_encounters']

print(f'Pokemon {pokemon} is {height} cm tall and {poke_type} is it type. You can find {pokemon} in {location_enc}')