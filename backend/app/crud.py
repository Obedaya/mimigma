from sqlalchemy.orm import Session
from models import RotorSettings
from schemas import RotorSettingsCreate

def get_rotor_settings(db: Session, user_id: int):
    return db.query(RotorSettings).filter(RotorSettings.user_id == user_id).first()

def create_or_update_rotor_settings(db: Session, settings: RotorSettingsCreate):
    db_settings = db.query(RotorSettings).filter(RotorSettings.user_id == settings.user_id).first()
    if db_settings:
        db_settings.machine_type = settings.machine_type
        db_settings.rotors = settings.rotors
        db_settings.rotor_positions = settings.rotor_positions
        db_settings.ring_positions = settings.ring_positions
    else:
        db_settings = RotorSettings(
            user_id=settings.user_id,
            machine_type=settings.machine_type,
            rotors=settings.rotors,
            rotor_positions=settings.rotor_positions,
            ring_positions=settings.ring_positions
        )
        db.add(db_settings)
    db.commit()
    db.refresh(db_settings)
    return db_settings
