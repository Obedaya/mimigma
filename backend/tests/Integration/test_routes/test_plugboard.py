import pytest
import requests

BASE_URL = "http://backend:9000"


@pytest.fixture(scope="module")
def base_url():
    return BASE_URL


def test_update_plugboard_setting(base_url):
    payload = {
        "user_id": 200,
        "plugboard": [["A", "H"], ["B", "I"], ["C", "J"]]
    }

    response = requests.post(f"{base_url}/plugboard", json=payload)
    print(response.json())
    assert response.status_code == 200

    data = response.json()
    assert "setting" in data
    assert data["setting"] == "Plugboard setting updated successfully"
