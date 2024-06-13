import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if (response.status_code != requests.codes.ok):
    print('coś poszło nie tak')
else:
    print(response.json())


requestsBody = {
    'title' : 'Nasz tytuł',
    'body' : 'treść posta',
    'userId' : 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=requestsBody)

if (response.status_code != requests.codes.created):
    print('coś poszło nie tak')
else:
    print(response.json())