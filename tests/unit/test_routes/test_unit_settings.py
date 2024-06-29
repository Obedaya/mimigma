import pytest
import app.routes.settings as settings
from app.database import SessionLocal
from app.models import Key, RotorSettings, ReflectorSettings
from app.crud import create_or_update_rotor_settings, create_or_update_reflector_settings
from app.schemas import RotorSettingCreate, ReflectorSettingCreate, PlugboardSettingCreate


def test_get_current_settings():
    db_session = SessionLocal()

    user_id = 200

    # Testdaten in die Datenbank einfügen
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

    existing_settings_reflector = db_session.query(ReflectorSettings).filter_by(user_id=user_id).first()

    if (existing_settings_reflector):
        existing_settings_reflector.user_id = user_id
        existing_settings_reflector.reflector = "UKW_N"
        create_or_update_reflector_settings(db_session, existing_settings_reflector)
    else:
        reflector_settings = ReflectorSettingCreate(
            user_id=user_id,
            reflector="UKW_N"
        )
        create_or_update_reflector_settings(db_session, reflector_settings)

    response = settings.get_current_settings(user_id)

    assert response == {"machine_type": "Enigma Norway", "rotors": ["IV", "V", "II"], "rotor_positions": "BBB", "ring_positions": "ZZZ", "reflector_type": "UKW_N", "plugboard": [["Z", "Z"]]}

    current_settings_rotor = db_session.query(RotorSettings).filter_by(user_id=user_id).first()
    current_settings_reflector = db_session.query(ReflectorSettings).filter_by(user_id=user_id).first()

    db_session.refresh(current_settings_rotor)
    db_session.refresh(current_settings_reflector)

    assert current_settings_rotor.machine_type == "Enigma Norway"
    assert current_settings_rotor.rotors == ["IV", "V", "II"]
    assert current_settings_rotor.rotor_positions == "BBB"
    assert current_settings_rotor.ring_positions == "ZZZ"
    assert current_settings_rotor.plugboard == [["Z", "Z"]]
    assert current_settings_reflector.reflector == "UKW_N"

