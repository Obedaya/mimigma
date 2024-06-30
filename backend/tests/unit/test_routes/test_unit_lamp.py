import pytest
import app.routes.lamp as lamp
from app.database import SessionLocal
from app.models import Key, RotorSettings, ReflectorSettings
from app.crud import create_or_update_rotor_settings, create_or_update_reflector_settings
from app.schemas import RotorSettingCreate, ReflectorSettingCreate


def test_get_encrypted_key():
    db_session = SessionLocal()

    user_id = 200

    # Testdaten in die Datenbank einfügen
    db_session.query(Key).delete()
    db_session.add(Key(key="A"))
    db_session.commit()

    rotor_settings = RotorSettingCreate(
        user_id=user_id,
        machine_type="Enigma M3",
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

    assert lamp.get_encrypted_key(user_id) == {"encrypted_key": "B"}

    # TODO: Überprüfen, ob die History korrekt gespeichert wurde