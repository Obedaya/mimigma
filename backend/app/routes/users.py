from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import User

router = APIRouter()

@router.get("/users", tags=["User Management"])
def read_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return [{"name": user.name, "username": user.username, "email": user.email} for user in users]
    finally:
        db.close()

