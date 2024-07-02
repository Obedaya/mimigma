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
    existing_settings = db_session.query(ReflectorSettings).filter_by(user_id=user_id).first()

    if (existing_settings):
        existing_settings.reflector = "UKW_N"
        db_session.commit()
        db_session.refresh(existing_settings)
    else:
        reflector_settings = ReflectorSettingCreate(
            user_id=user_id,
            reflector="UKW_N"
        )

        # Testdaten in die Datenbank einfügen
        create_or_update_reflector_settings(db_session, reflector_settings)

    response = reflector.update_reflector_setting(user_id, "UKW_B")

    # Assert result
    assert response == {"message": "Rotor setting created successfully"}

    current_settings = db_session.query(ReflectorSettings).filter_by(user_id=user_id).first()
    db_session.refresh(current_settings)

    assert current_settings.reflector == "UKW_B"

    db_session.query(ReflectorSettings).filter_by(user_id=user_id).delete()
    db_session.commit()

    response = reflector.update_reflector_setting(user_id, "UKW_B")

    # Assert result
    assert response == {"message": "Rotor setting created successfully"}

    current_settings = db_session.query(ReflectorSettings).filter_by(user_id=user_id).first()
    db_session.refresh(current_settings)

    assert current_settings.reflector == "UKW_B"

    db_session.close()
