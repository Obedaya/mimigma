import pytest
import app.routes.reflector as reflector
from app.database import SessionLocal
from app.models import Key, RotorSettings, ReflectorSettings
from app.crud import create_or_update_rotor_settings, create_or_update_reflector_settings
from app.schemas import RotorSettingCreate, ReflectorSettingCreate


def test_update_plugboard_setting():
    db_session = SessionLocal()

    user_id = 200

    # Testdaten in die Datenbank einfügen
    existing_settings = db_session.query(RotorSettings).filter_by(user_id=user_id).first()

    if (existing_settings):
        existing_settings.plugboard = [["Z", "Z"]]
        db_session.commit()
        db_session.refresh(existing_settings)
    else:
        rotor_settings = RotorSettingCreate(
            user_id=user_id,
            machine_type="Enigma M3",
            rotors=["I", "II", "III"],
            rotor_positions="AAA",
            ring_positions="AAA",
            plugboard=[["Z", "Z"]]
        )
        reflector_settings = ReflectorSettingCreate(
            user_id=user_id,
            reflector="UKW_B"
        )

        # Testdaten in die Datenbank einfügen
        create_or_update_rotor_settings(db_session, rotor_settings)
        create_or_update_reflector_settings(db_session, reflector_settings)

    data = {
        "user_id": user_id,
        "plugboard": [["A", "B"]]
    }

    response = plugboard.update_plugboard_setting(PlugboardSettingCreate(**data))

    # Assert result
    assert response == {"setting": "Plugboard setting updated successfully"}

    current_settings = db_session.query(RotorSettings).filter_by(user_id=user_id).first()
    db_session.refresh(current_settings)

    assert current_settings.plugboard == [["A", "B"]]
