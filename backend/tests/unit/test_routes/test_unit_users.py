import pytest
import app.routes.users as users
from app.database import SessionLocal
from app.models import Key, RotorSettings, ReflectorSettings, Base, User
from app.crud import create_or_update_rotor_settings, create_or_update_reflector_settings
from app.schemas import RotorSettingCreate, ReflectorSettingCreate
from app.utils import hash_password

def test_read_users():
    db_session = SessionLocal()
    if not (db_session.query(User).filter(User.username == "testuser").first()):
        hashed_password = hash_password("testpassword")
        db_session.add(User(id=200, name="Test User", username="testuser", email="testuser@email.com", password=hashed_password))
        db_session.commit()

    response = users.read_users()

    response = [response[-1]]

    assert response == [{"name": "Test User", "username": "testuser", "email": "testuser@email.com"}]