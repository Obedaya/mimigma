from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import sessionmaker, Session

from ..schemas import ReflectorSettingCreate
from ..crud import get_reflector_settings
from ..database import get_db, SessionLocal, engine
from ..models import ReflectorSettings, Base


router = APIRouter()

Base.metadata.create_all(bind=engine)

@router.get("/reflector", tags=["Reflector"])
def read_reflector_setting():
    db = SessionLocal()
    try:
        # Logic to set the reflector setting
        return {"message": "Reflector setting retrieved successfully"}
    finally:
        db.close()

# axios.post(`/reflector?uid=${auth.currenUserID}?reflector={selectedReflectorOption}`)
@router.post("/reflector", tags=["Reflector"])
def update_reflector_setting(user_id: int, reflector: str):
    db = SessionLocal()
    try:
        existing_setting = db.query(ReflectorSettings).filter_by(user_id=user_id).first()

        if existing_setting:
            existing_setting.user_id = user_id
            existing_setting.reflector = reflector
            db.commit()
            db.refresh(existing_setting)
            message = "Reflector setting updated successfully"
        else:
            # Insert new record
            reflector_setting = ReflectorSettings(
                user_id = user_id,
                reflector = reflector,
            )
            db.add(reflector_setting)
            db.commit()
            db.refresh(reflector_setting)
            message = "Reflector setting created successfully"

        # Logic to update the reflector setting in the database
        print(f"User ID: {user_id}")
        print(f"Reflector: {reflector}")
        message = "Rotor setting created successfully"
        return {"message": message}
    finally:
        db.close()
