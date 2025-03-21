import requests
import models
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import Session


class Create_Crypto_data(BaseModel):
    value : float
    volume : float
    currency : str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


headers = {
    "Accept-Encoding": "gzip",
    "Authorization": 'f1d08495-bf45-4892-a639-b5414bc5c38d'
}


def take_data(cryptocurrency: str):
    response = requests.get(f'https://api.coincap.io/v2/assets/{cryptocurrency}', headers=headers)

    crypto_data = response.json()

    value = crypto_data['data']['priceUsd']
    volume = crypto_data['data']['volumeUsd24Hr']
    currency = crypto_data['data']['name']

    return [value, volume, currency]


def validate(name: str):

    response = requests.get(f'https://api.coincap.io/v2/assets/{name}', headers=headers)

    if response.status_code == 200:
        return True
    return False

#day check_up 2
#day chack_up 3





