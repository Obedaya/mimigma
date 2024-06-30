import pytest
import requests

BASE_URL = "http://backend:9000"

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL


def test_update_reflector_setting(base_url):
    payload = {
        "user_id": 1,
        "reflector": "UKW_B"
    }
    response = requests.post(f"{base_url}/reflector", params=payload)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Rotor setting created successfully"
