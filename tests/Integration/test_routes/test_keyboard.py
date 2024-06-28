import pytest
import requests

BASE_URL = "http://backend:9000"

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL

def test_post_keyboard(base_url):
    response = requests.post(f"{base_url}/keyboard?key=A")
    assert response.status_code == 200

def test_get_keyboard(base_url):
    response = requests.get(f"{base_url}/keyboard")
    assert response.status_code == 200

    data = response.json()
    assert "key" in data
    assert isinstance(data["key"], dict)
    assert data.get("key").get("key") == "A"
