from fastapi import APIRouter, Request, HTTPException, status
from ..database import SessionLocal
from ..models import User
from ..utils import hash_password

router = APIRouter()

# Stephane : Endpoint to check user Login
@router.post("/login", tags=["User Management"])
async def login(username: str, password: str):
    db = SessionLocal()
    try:
        hashed_password = hash_password(password)
        user = db.query(User).filter(User.username == username, User.password == hashed_password).first()
        if user:
            return {"message": "Login successful"}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    finally:
        db.close()

