import requests

headers = {
    "Accept-Encoding": "gzip",
    "Authorization": 'f1d08495-bf45-4892-a639-b5414bc5c38d'
}


def take_data(cryptocurrency: str):
    response = requests.get(f'https://api.coincap.io/v2/assets/{cryptocurrency}', headers=headers)

    crypto_data = response.json()

    id = crypto_data['data']['id']
    value = crypto_data['data']['priceUsd']
    volume = crypto_data['data']['volumeUsd24Hr']
    currency = crypto_data['data']['name']

    return [id, value, volume, currency]


def validate(name: str):

    response = requests.get(f'https://api.coincap.io/v2/assets/{name}', headers=headers)

    if response.status_code == 200:
        return True
    return False

