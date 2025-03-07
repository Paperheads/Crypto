from datetime import timedelta, datetime, timezone
from http.client import HTTPException
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

from database import SessionLocal
from models import Users, CryptoData, Crypto
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, UTC
from jose import jwt, JWTError

from parser.pars_data import validate

router = APIRouter(
    prefix="/crypto",
    tags=["crypto"]
)

class CreateCrypto(BaseModel):
    name : str
    title : str
    data: datetime = Field(default_factory=lambda: datetime.now(UTC))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    cryptos = db.query(Crypto).all()

    result = []
    for crypto in cryptos:
        result.append({
            "id": crypto.id,
            "name": crypto.name,
            "title": crypto.title,
            "data": crypto.data,

            "details": [
                {
                    "id": details.id,
                    "value": details.value,
                    "volume": details.volume,
                    "currency": details.currency,
                }
                for details in crypto.details
            ]
        })

    return result


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def read_by_id(id: int, db : db_dependency):
    crypto = db.query(Crypto).filter(Crypto.id == id).first()
    return crypto


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_crypto(db: db_dependency, create_crypto: CreateCrypto):
    create_crypto = Crypto(
        name = create_crypto.name,
        title = create_crypto.title,
    )


    if validate(create_crypto.name):
        db.add(create_crypto)
        db.commit()

    else:
        raise HTTPException(status_code=400, detail="Invalid cryptocurrency data")