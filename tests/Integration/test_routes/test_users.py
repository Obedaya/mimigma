import pytest
import requests

BASE_URL = "http://backend:9000"

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL

def test_read_users(base_url):
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
