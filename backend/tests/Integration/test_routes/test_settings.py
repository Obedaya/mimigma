import pytest
import requests

BASE_URL = "http://backend:9000"


@pytest.fixture(scope="module")
def base_url():
    return BASE_URL


def test_get_current_settings(base_url):
    user_id = 200

    response = requests.get(f"{base_url}/settings?user_id={user_id}")
    assert response.status_code == 200

    data = response.json()
    assert "machine_type" in data
    assert "rotors" in data
    assert "rotor_positions" in data
    assert "ring_positions" in data
    assert "reflector_type" in data

    # assert data["machine_type"] == "Enigma I"
    # assert data["rotors"] == ["I", "II", "III"]
    # assert data["rotor_positions"] == "AAA"
    # assert data["ring_positions"] == "AAA"
    # assert data["reflector_type"] == "UKW_B"
