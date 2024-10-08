import pytest
from app.database import SessionLocal
from app.models import RotorSettings
import app.routes.rotor as rotor
from app.schemas import RotorSettingCreate
from app.crud import create_or_update_rotor_settings


# Helper function to create test data
def create_rotor_setting(user_id, machine_type, rotors, rotor_positions, ring_positions, plugboard):
    return RotorSettings(
        user_id=user_id,
        machine_type=machine_type,
        rotors=rotors,
        rotor_positions=rotor_positions,
        ring_positions=ring_positions,
        plugboard=plugboard
    )

# Setup and Teardown
@pytest.fixture(scope='function')
def setup_db():
    db_session = SessionLocal()
    yield db_session
    db_session.rollback()
    db_session.close()

def test_update_rotor_settings():
    db_session = SessionLocal()
    
    user_id = 200

 
    existing_settings_rotor = db_session.query(RotorSettings).filter_by(user_id=user_id).first()

    if (existing_settings_rotor):
        existing_settings_rotor.user_id = user_id
        existing_settings_rotor.machine_type = "Enigma Norway"
        existing_settings_rotor.rotors = ["IV", "V", "II"]
        existing_settings_rotor.rotor_positions = "BBB"
        existing_settings_rotor.ring_positions = "ZZZ"
        existing_settings_rotor.plugboard = [["Z", "Z"]]

        create_or_update_rotor_settings(db_session, existing_settings_rotor)
    else:
        rotor_settings = RotorSettingCreate(
            user_id=user_id,
            machine_type="Enigma Norway",
            rotors=["IV", "V", "II"],
            rotor_positions="BBB",
            ring_positions="ZZZ",
            plugboard=[["Z", "Z"]]
        )

        # Testdaten in die Datenbank einfügen
        create_or_update_rotor_settings(db_session, rotor_settings)

    # Testdaten vorbereiten
    new_settings = create_rotor_setting(
        user_id=user_id,
        machine_type="Enigma M3",
        rotors=["II", "IV", "V"],
        rotor_positions="BBB",
        ring_positions="AAA",
        plugboard=[["A", "B"]]
    )

    # Funktion aufrufen
    rotor.update_rotor_setting(new_settings)


    # Ergebnis überprüfen
    updated_settings = db_session.query(RotorSettings).filter_by(user_id=user_id).first()
    db_session.refresh(updated_settings)
    assert updated_settings.machine_type == "Enigma M3"
    assert updated_settings.rotors == ["II", "IV", "V"]
    assert updated_settings.rotor_positions == "BBB"
    assert updated_settings.ring_positions == "AAA"
    assert updated_settings.plugboard == [["A", "B"]]

    # Testdaten löschen
    db_session.query(RotorSettings).filter_by(user_id=user_id).delete()
    db_session.commit()

    # Testdaten überprüfen
    rotor.update_rotor_setting(new_settings)

    # Ergebnis überprüfen
    updated_settings = db_session.query(RotorSettings).filter_by(user_id=user_id).first()
    db_session.refresh(updated_settings)
    assert updated_settings.machine_type == "Enigma M3"
    assert updated_settings.rotors == ["II", "IV", "V"]
    assert updated_settings.rotor_positions == "BBB"
    assert updated_settings.ring_positions == "AAA"
    assert updated_settings.plugboard == [["A", "B"]]

    db_session.close()

def test_update_rotor_position():
    db_session = SessionLocal()

    user_id = 200

    existing_settings_rotor = db_session.query(RotorSettings).filter_by(user_id=user_id).first()

    if (existing_settings_rotor):
        existing_settings_rotor.user_id = user_id
        existing_settings_rotor.machine_type = "Enigma Norway"
        existing_settings_rotor.rotors = ["IV", "V", "II"]
        existing_settings_rotor.rotor_positions = "BBB"
        existing_settings_rotor.ring_positions = "ZZZ"
        existing_settings_rotor.plugboard = [["Z", "Z"]]

        create_or_update_rotor_settings(db_session, existing_settings_rotor)
    else:
        rotor_settings = RotorSettingCreate(
            user_id=user_id,
            machine_type="Enigma Norway",
            rotors=["IV", "V", "II"],
            rotor_positions="BBB",
            ring_positions="ZZZ",
            plugboard=[["Z", "Z"]]
        )

        # Testdaten in die Datenbank einfügen
        create_or_update_rotor_settings(db_session, rotor_settings)

    # Funktion aufrufen
    rotor.update_rotor_position(user_id, "AAA")

    # Ergebnis überprüfen
    updated_settings = db_session.query(RotorSettings).filter_by(user_id=user_id).first()
    db_session.refresh(updated_settings)
    assert updated_settings.rotor_positions == "AAA"

    db_session.close()

def test_rotor_count():
    db_session = SessionLocal()

    # Funktion aufrufen
    rotor_count = rotor.rotor_count(3)

    # Ergebnis überprüfen
    assert rotor_count == {"message": "Rotor count retrieved successfully"}

    db_session.close()

def test_standard_rotor():
    db_session = SessionLocal()

    # Funktion aufrufen
    standard_rotor = rotor.standard_rotor("Enigma I")

    # Ergebnis überprüfen
    assert standard_rotor == {"turnovers": {"I": "Q", "II": "E", "III": "V", "IV": "J", "V": "Z"}}

    standard_rotor = rotor.standard_rotor("Enigma M3")

    assert standard_rotor == {"turnovers": {"I": "Q", "II": "E", "III": "V", "IV": "J", "V": "Z", "VI": "ZM", "VII": "ZM", "VIII": "ZM"}}

    standard_rotor = rotor.standard_rotor("Enigma Norway")

    assert standard_rotor == {"turnovers": {"I": "Q", "II": "E", "III": "V", "IV": "J", "V": "Z"}}

    standard_rotor = rotor.standard_rotor("Custom Enigma")

    assert standard_rotor == {"turnovers": {"I": "Q", "II": "E", "III": "V", "IV": "J", "V": "Z", "VI": "ZM", "VII": "ZM", "VIII": "ZM"}}


