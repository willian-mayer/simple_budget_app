from fastapi import FastAPI
from app.routers import account
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(account.router)
