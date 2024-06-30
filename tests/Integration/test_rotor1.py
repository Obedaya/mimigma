import pytest
from app.database import engine, check_db_connection, get_db, SessionLocal
from app.init_db import init_db
from app.models import RotorSettings
from app.crud import get_rotor_settings
from app.enigma.rotor import get_rotor_settings_from_db
from fastapi import HTTPException


@pytest.fixture
def db_session():
    check_db_connection(engine)
    init_db()
    get_db()

    test_settings = RotorSettings(
        user_id=1,
        machine_type="Enigma I",
        rotors=["I", "II", "III"],
        rotor_positions=["AAA"],
        ring_positions=["AAA"]
    )


def test_get_rotor_settings_from_db(db_session):
    db_session = SessionLocal()
    settings = get_rotor_settings_from_db(user_id=1, db=db_session)
    assert settings == ("Enigma I", ["I", "II", "III"], "BBB", "AAA")

    with pytest.raises(HTTPException) as exc_info:
        get_rotor_settings_from_db(user_id=2, db=db_session)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Settings not found"