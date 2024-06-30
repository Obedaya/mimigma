import pytest
import app.routes.keyboard as keyboard
from app.models import Key, History
from fastapi import HTTPException
from app.crud import create_or_update_rotor_settings, create_or_update_reflector_settings
from app.schemas import RotorSettingCreate, ReflectorSettingCreate
from app.database import check_db_connection, engine, get_db, SessionLocal
from app.models import RotorSettings, ReflectorSettings
from sqlalchemy import desc
from sqlalchemy.orm import Session

def test_post_keyboard():
    db_session = SessionLocal()

    user_id = 200

    key = "Z"
    db_session.query(Key).delete()
    db_session.add(Key(key=key))
    db_session.commit()

    test_key = "A"

    keyboard.post_keyboard(test_key, user_id)

    assert db_session.query(Key).first().key == test_key

    db_session = SessionLocal()
    key = "A"
    db_session.query(History).filter(History.user_id == user_id).delete()
    db_session.commit()


    keyboard.post_keyboard(key, user_id)

    # Check the result
    latest_history = db_session.query(History).order_by(desc(History.id)).first()

    assert latest_history.plain == "A"
    assert latest_history.encrypted == ""

def test_get_keyboard():
    db_session = SessionLocal()

    key = "Z"
    db_session.query(Key).delete()
    db_session.add(Key(key=key))
    db_session.commit()

    response = keyboard.get_keyboard()

    extracted_key = response["key"].key

    assert extracted_key == key
