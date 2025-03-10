from http.client import HTTPException
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

from database import SessionLocal
from models import Users, CryptoData, Crypto
from datetime import datetime, UTC

from parser.pars_data import validate

router = APIRouter(
    prefix="/crypto",
    tags=["crypto"]
)


class CreateCrypto(BaseModel):
    name: str
    title: str
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
async def read_by_id(id: int, db: db_dependency):
    crypto = db.query(Crypto).filter(Crypto.id == id).first()
    return crypto


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_crypto(db: db_dependency, create_crypto: CreateCrypto):
    create_crypto = Crypto(
        name=create_crypto.name,
        title=create_crypto.title,
    )

    if validate(create_crypto.name):
        db.add(create_crypto)
        db.commit()

    else:
        raise HTTPException(status_code=400, detail="Invalid cryptocurrency data")


@router.delete("crypto/{crypto_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_crypto(db: db_dependency, crypto_id: int = Path(gt=0)):

    crypto = db.query(Crypto).filter(Crypto.id == crypto_id).first()

    if crypto is None:
        raise HTTPException(status_code=404, detail="Crypto not found")

    db.query(Crypto).filter(Crypto.id == crypto.id).delete()
    db.commit()


