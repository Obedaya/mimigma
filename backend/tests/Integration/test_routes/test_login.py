import pytest
import requests
from app.database import SessionLocal
from app.models import User
from app.utils import hash_password

BASE_URL = "http://backend:9000"

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL


def test_login_success(base_url):
    db_session = SessionLocal()
    if not (db_session.query(User).filter(User.username == "testuser").first()):
        hashed_password = hash_password("testpassword")
        db_session.add(User(id=200, name="Test User", username="testuser", email="testuser@email.com", password=hashed_password))
        db_session.commit()

    response = requests.post(f"{base_url}/login?username=testuser&password=testpassword")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert data["message"] == "Login successful"
    assert "user" in data
    assert "access_token" in data


def test_login_failure(base_url):
    response = requests.post(f"{base_url}/login?username=user_test_2&password=wrongpassword")
    assert response.status_code == 401

    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Invalid username or password"
