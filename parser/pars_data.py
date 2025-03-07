import requests

headers = {
    "Accept-Encoding": "gzip",
    "Authorization": 'f1d08495-bf45-4892-a639-b5414bc5c38d'
}



def take_data(cryptocurrency : str):

    response = requests.get(f'https://api.coincap.io/v2/assets/{cryptocurrency}', headers=headers)

    return response.json()

b = take_data('bitcoin')

for i in b['data']:
    print(f"The category {i} is {b['data'][i]}")
