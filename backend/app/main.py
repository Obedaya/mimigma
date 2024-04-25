from typing import Union
import os
from fastapi import FastAPI, HTTPException # Importiere Klassen aus dem FastAPI-Framework und die HTTPException-Klasse für Fehlerbehandlung.
from sqlalchemy import create_engine, Column, Integer, String # Importiere Funktionen und Klassen aus SQLAlchemy für ORM.
from sqlalchemy.ext.declarative import declarative_base # Importiere Funktion für Basisdeklaration von Modellen in SQLAlchemy.
from sqlalchemy.orm import sessionmaker # Importiere die sessionmaker-Funktion, um Datenbanksitzungen zu erstellen.

app = FastAPI()

#DATABASE_URL = "postgresql://db_user:db_pass@db/enigma_db"

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Create all tables in the db automatically based on the model 
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    db = SessionLocal()
    try:
        # Check if there are any users already
        if db.query(User).count() == 0:
            db.add_all([
                User(name="Alice"),
                User(name="Bob"),
                User(name="Mallory")
            ])
            db.commit()
    finally:
        db.close()
@app.get("/users/")
def read_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return [{"name": user.name} for user in users]
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
