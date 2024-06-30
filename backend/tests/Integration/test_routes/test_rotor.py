import pytest
import requests

BASE_URL = "http://backend:9000"

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL

def test_update_rotor_setting(base_url):
    payload = {
        "user_id": 1,
        "machine_type": "Enigma I",
        "rotors": ["I", "II", "III"],
        "rotor_positions": "AAA",
        "ring_positions": "AAA",
        "plugboard": [["A", "H"], ["B", "I"], ["C", "J"]]
    }
    response = requests.post(f"{base_url}/rotor", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] in ["Rotor setting created successfully", "Rotor setting updated successfully"]

def test_update_rotor_position(base_url):
    response = requests.post(f"{base_url}/rotor/position?user_id=1&position=BBB")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Rotor position set successfully"

def test_rotor_count(base_url):
    response = requests.post(f"{base_url}/rotor/count?count=3")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Rotor count retrieved successfully"

def test_standard_rotor(base_url):
    response = requests.get(f"{base_url}/rotor/standard?variant=Enigma%20I")
    assert response.status_code == 200
    data = response.json()
    assert "turnovers" in data
    assert data["turnovers"] == {"I": "Q", "II": "E", "III": "V", "IV": "J", "V": "Z"}
