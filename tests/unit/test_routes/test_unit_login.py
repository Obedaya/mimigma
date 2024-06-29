import pytest
import app.routes.login as login
import jwt
from app.database import SessionLocal
from app.models import Key, RotorSettings, ReflectorSettings, Base, User
from app.crud import create_or_update_rotor_settings, create_or_update_reflector_settings
from app.schemas import RotorSettingCreate, ReflectorSettingCreate
from datetime import datetime, timedelta
from app.utils import hash_password


def test_create_access_token():
    data = {"user_id": 1}
    data.update({"exp": datetime.utcnow() + timedelta(minutes=15)})
    assert login.create_access_token(data) == jwt.encode(data, "secret_key", algorithm="HS256")

async def test_login():
    db_session = SessionLocal()
    if not (db_session.query(User).filter(User.username == "testuser").first()):
        hashed_password = hash_password("testpassword")
        db_session.add(User(id=200, name="Test User", username="testuser", email="testuser@email.com", password=hashed_password))
        db_session.commit()

    response = await login.login("testuser", "testpassword")
    assert response == {
        "message": "Login successful",
        "user": {
            "id": 200,
            "username": "testuser"
        },
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MTk2NTg3MDZ9.47zdxiglMo08g171x6H8mpyqHVUxFxqF7HLITKpuMII"
    }

    assert login.login("testuser", "wrongpassword") == {
        "Invalid username or password"
    }

    assert login.login("wronguser", "testpassword") == {
        "Invalid username or password"
    }