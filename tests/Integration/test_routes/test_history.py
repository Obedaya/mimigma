import pytest
import requests

BASE_URL = "http://backend:9000"

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL

def test_get_history(base_url):
    response = requests.get(f"{base_url}/history")
    assert response.status_code == 200

    data = response.json()
    assert "plain" in data
    assert "encrypted" in data

def test_delete_history(base_url):
    response = requests.get(f"{base_url}/deletehistory")
    assert response.status_code == 200

    data = response.json()
    assert data == {"message": "History cleared."}
