from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from ..database import get_db, SessionLocal
from ..crud import create_or_update_rotor_settings, create_or_update_reflector_settings
from ..schemas import RotorSettingCreate, ReflectorSettingCreate

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/reset")
def reset(user_id: int):
    db = SessionLocal()
    try:
        default_rotor_settings = {
            "user_id": user_id,
            "machine_type": "M3",
            "rotors": ["I", "II", "III"],
            "rotor_positions": "AAA",
            "ring_positions": "AAA"
        }
        default_reflector_settings = {
            "user_id": user_id,
            "reflector": "UKW_B"
        }
        default_rotor_settings = RotorSettingCreate(**default_rotor_settings)
        default_reflector_settings = ReflectorSettingCreate(**default_reflector_settings)
        create_or_update_rotor_settings(db, default_rotor_settings)
        create_or_update_reflector_settings(db, default_reflector_settings)
        return {"message": "Reset successful"}
    except Exception as e:
        print(f"Exception: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()


