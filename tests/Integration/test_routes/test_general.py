from backend.app.crud import create_or_update_rotor_settings, create_or_update_reflector_settings
from backend.app.schemas import RotorSettingCreate, ReflectorSettingCreate
from backend.app.database import check_db_connection, engine, get_db
from backend.app.init_db import init_db
from backend.app.models import RotorSettings, ReflectorSettings
import requests
import pytest


BASE_URL = "http://localhost:8080"

@pytest.fixture(scope="function")
def db_session():
    check_db_connection(engine)
    init_db()
    get_db()

def test_read_root():

    response = requests.get(f"{BASE_URL}/")
    expected_response = {"Hello": "World"}
    assert response.status_code == 200
    assert response.json() == expected_response


def test_reset_rotor_and_reflector_settings(db_session):
    # Test: Rotor- und Reflektor-Einstellungen zurücksetzen
    user_id = 1  # Beispiel-Wert für user_id
    rotor_settings = RotorSettingCreate(
        user_id=user_id,
        machine_type="Enigma I",
        rotors=["I", "II", "III"],
        rotor_positions="AAA",
        ring_positions="AAA",
        plugboard=[]
    )
    reflector_settings = ReflectorSettingCreate(
        user_id=user_id,
        reflector="UKW_B"
    )

    # Testdaten in die Datenbank einfügen
    create_or_update_rotor_settings(db_session, rotor_settings)
    create_or_update_reflector_settings(db_session, reflector_settings)

    """def test_reset_http_request():
        user_id = 1

        response = requests.get(f"{BASE_URL}/rest", json={"user_id": user_id})
        expected_response = {"message": "Reset successful"}
        assert response.status_code == 200
        assert response.json() == expected_response"""

    # Überprüfen, ob die Daten zurückgesetzt wurden
    updated_rotor_settings = db_session.query(RotorSettings).filter_by(user_id=user_id).first()
    updated_reflector_settings = db_session.query(ReflectorSettings).filter_by(user_id=user_id).first()

    assert updated_rotor_settings is not None
    assert updated_rotor_settings.machine_type == "Enigma I"
    assert updated_rotor_settings.rotors == ["I", "II", "III"]
    assert updated_rotor_settings.rotor_positions == "AAA"
    assert updated_rotor_settings.ring_positions == "AAA"
    assert updated_rotor_settings.plugboard == []

    assert updated_reflector_settings is not None
    assert updated_reflector_settings.reflector == "UKW_B"











