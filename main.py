from fastapi import FastAPI
import models
from database import engine
from routers import auth, crypto

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(crypto.router)
