from typing import Union
import os
from fastapi import FastAPI, HTTPException 
from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base # import function for base declaration 
from sqlalchemy.orm import sessionmaker

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

# Will create all tables in the db automatically  
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
