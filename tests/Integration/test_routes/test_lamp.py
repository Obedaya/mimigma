import pytest
import requests

BASE_URL = "http://backend:9000"

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL

def test_get_encrypted_key(base_url):
    user_id = 1
    response = requests.get(f"{base_url}/lamp?user_id={user_id}")
    assert response.status_code == 200

    data = response.json()
    assert "encrypted_key" in data
    assert isinstance(data["encrypted_key"], str)
    assert data["encrypted_key"] != ""