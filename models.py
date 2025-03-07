from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean)
    role = Column(String)


class Crypto(Base):
    __tablename__ = 'crypto'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    title = Column(String)
    data = Column(String)

    owner_id = Column(Integer, ForeignKey('users.id'))

    details = relationship("CryptoData", back_populates="crypto")


    
class CryptoData(Base):
    __tablename__ = 'crypto_data'
    
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer)
    volume = Column(Integer)
    currency = Column(String)

    owner_id = Column(Integer, ForeignKey('crypto.id'))

    crypto = relationship("Crypto", back_populates="details")
