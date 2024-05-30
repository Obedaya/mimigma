import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, status
from ..database import SessionLocal
from ..models import User
from ..utils import hash_password

SECRET_KEY = "your_secret_key"  # Ersetzen Sie dies durch einen sichereren Schlüssel
ALGORITHM = "HS256"

router = APIRouter()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Endpoint to check user login
@router.post("/login", tags=["User Management"])
async def login(username: str, password: str):
    db = SessionLocal()
    try:
        hashed_password = hash_password(password)
        user = db.query(User).filter(User.username == username, User.password == hashed_password).first()
        if user:
            access_token = create_access_token(data={"user_id": user.id})
            return {
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "username": user.username,
                },
                "access_token": access_token
            }
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    finally:
        db.close()
