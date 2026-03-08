from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import models, database
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Stride Type API")

@app.get("/")
def health_check():
    return {"status": "online", "database": "connected"}