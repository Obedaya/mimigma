from typing import Union
import os, time
from fastapi import FastAPI, HTTPException 
from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base # import function for base declaration 
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

# check if the database is connected
def check_db_connection(engine):
    while True:
        try:
            # try to connect the db
            with engine.connect() as conn:
                # when the connection is successful, break the loop
                break
        except Exception as e:
            print ("Waiting for database connection...")
            print(e)
            # wait 2 seconds before connecting again
            time.sleep(2)
            
#create database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)




@app.on_event("startup")
async def startup_event():
    check_db_connection(engine)
    db = SessionLocal()
    # once the db is connected, create all tables
    Base.metadata.create_all(bind=engine)
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
