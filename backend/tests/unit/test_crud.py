"""import pytest
import logging
from app.models import RotorSettings, ReflectorSettings
from app.schemas import RotorSettingCreate, ReflectorSettingCreate
from app.crud import (get_rotor_settings, get_reflector_settings,
                    create_or_update_rotor_settings, create_or_update_reflector_settings)
from app.database import check_db_connection, engine, get_db, SessionLocal
from app.init_db import init_db


@pytest.fixture(scope="function")
def db_session():
    check_db_connection(engine)
    init_db()
    get_db()
    yield
def test_get_rotor_settings(db_session):
    db_session = SessionLocal()
    user_id = 1
    rotor_settings = RotorSettings(
        user_id=user_id,
        machine_type="Enigma I",
        rotors=["I", "II", "III"],
        rotor_positions="AAA",
        ring_positions="AAA",
        plugboard=[]
    )
    db_session.add(rotor_settings)
    db_session.commit()

    result = get_rotor_settings(db_session, user_id)
    assert result is not None
    assert result.user_id == user_id
    assert result.machine_type == "Enigma I"

def test_create_or_update_rotor_settings(db_session):
    user_id = "1"
    settings = RotorSettingCreate(
        user_id=user_id,
        machine_type="Enigma I",
        rotors=["I", "II", "III"],
        rotor_positions="AAA",
        ring_positions="AAA",
        plugboard=[]
    )

    result = create_or_update_rotor_settings(db_session, settings)
    assert result is not None
    assert result.user_id == user_id
    assert result.machine_type == "Enigma I"

    updated_settings = RotorSettingCreate(
        user_id=user_id,
        machine_type="Enigma I",
        rotors=["I", "II", "III"],
        rotor_positions="AAA",
        ring_positions="AAA",
        plugboard=[]
    )

    updated_result = create_or_update_rotor_settings(db_session, updated_settings)
    assert updated_result is not None
    assert updated_result.user_id == user_id
    assert updated_result.machine_type == "Enigma I"

def test_get_reflector_settings(db_session):
    user_id = 2
    reflector_settings = ReflectorSettings(
        user_id=user_id,
        reflector="UKW_A"
    )
    db_session.add(reflector_settings)
    db_session.commit()

    result = get_reflector_settings(db_session, user_id)
    assert result is not None
    assert result.user_id == user_id
    assert result.reflector == "UKW_A"


def test_create_or_update_reflector_settings(db_session):
    user_id = 4
    settings = ReflectorSettingCreate(
        user_id=user_id,
        reflector="UKW_B"
    )

    result = create_or_update_reflector_settings(db_session, settings)
    assert result is not None
    assert result.user_id == user_id
    assert result.reflector == "UKW_B"""
