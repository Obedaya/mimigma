import pytest
import app.routes.general as general
from fastapi import HTTPException
from app.crud import create_or_update_rotor_settings, create_or_update_reflector_settings
from app.schemas import RotorSettingCreate, ReflectorSettingCreate
from app.database import check_db_connection, engine, get_db, SessionLocal
from app.models import RotorSettings, ReflectorSettings


def test_read_root():
    assert general.read_root() == {"status": "ok"}


def test_reset():
    db_session = SessionLocal()
    user_id = 200

    rotor_settings = RotorSettingCreate(
        user_id=user_id,
        machine_type="Enigma M3",
        rotors=["II", "IV", "II"],
        rotor_positions="CFB",
        ring_positions="GBD",
        plugboard=[["A", "B"], ["C", "D"]]
    )
    reflector_settings = ReflectorSettingCreate(
        user_id=user_id,
        reflector="UKW_B"
    )

    # Testdaten in die Datenbank einfügen
    create_or_update_rotor_settings(db_session, rotor_settings)
    create_or_update_reflector_settings(db_session, reflector_settings)

    assert general.reset(user_id) == {"message": "Reset successful"}

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
    db_session.close()
