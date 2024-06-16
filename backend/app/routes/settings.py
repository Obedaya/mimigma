from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from ..database import get_db, SessionLocal
from ..enigma.rotor import get_rotor_settings_from_db
from ..crud import get_rotor_settings, get_reflector_settings

router = APIRouter()

@router.get("/settings", tags=["Settings"])
def get_current_settings(user_id: int):
    db = SessionLocal()
    try:
        rotor_settings = get_rotor_settings(db, user_id)
        reflector_settings = get_reflector_settings(db, user_id)

        machine_type = rotor_settings.machine_type
        rotors = rotor_settings.rotors
        rotor_positions = rotor_settings.rotor_positions
        ring_positions = rotor_settings.ring_positions
        reflector_type = reflector_settings.reflector

        print(f"Machine type: {machine_type}, Rotors: {rotors}, Rotor positions: {rotor_positions}, Ring positions: {ring_positions}, Reflector type: {reflector_type}")

        return {"machine_type": machine_type, "rotors": rotors, "rotor_positions": rotor_positions, "ring_positions": ring_positions, "reflector_type": reflector_type}
    except Exception as e:
        print(f"Exception: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()