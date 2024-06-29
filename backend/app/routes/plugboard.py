from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..crud import get_rotor_settings
from ..models import RotorSettings, Base
from typing import List
from ..schemas import PlugboardSettingCreate

router = APIRouter()


@router.post("/plugboard", tags=["Plugboard"])
def update_plugboard_setting(data: PlugboardSettingCreate):
    db = SessionLocal()
    try:
        # Logic to update the plugboard setting in the database
        existing_settings = db.query(RotorSettings).filter_by(user_id=data.user_id).first()

        # Update plugboard
        existing_settings.plugboard = data.plugboard
        print(f"Plugboard setting: {existing_settings.plugboard}")

        db.commit()
        db.refresh(existing_settings)

        return {"setting": "Plugboard setting updated successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        db.close()