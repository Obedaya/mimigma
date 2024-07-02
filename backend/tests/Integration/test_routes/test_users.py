import pytest
import requests
from app.database import SessionLocal
from app.models import User
from app.utils import hash_password

BASE_URL = "http://backend:9000"

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL

def test_read_users(base_url):
    db_session = SessionLocal()
    if not (db_session.query(User).filter(User.username == "testuser").first()):
        hashed_password = hash_password("testpassword")
        db_session.add(User(id=200, name="Test User", username="testuser", email="testuser@email.com", password=hashed_password))
        db_session.commit()

    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    if data:
        user = data[0]
        assert "name" in user
        assert "username" in user
        assert "email" in user

    # assert user["name"] == "John Doe"
    # assert user["username"] == "johndoe"
    # assert user["email"] == "johndoe@example.com"
