from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from ..database import get_db, SessionLocal
from ..models import Key
from ..enigma.enigma import Enigma
from ..enigma.rotor import get_rotor_settings_from_db

router = APIRouter()

user_id = 4

@router.get("/lamp", tags=["Lamp"])
def get_encrypted_key():
    db = SessionLocal()
    # try:
    #     current_key = db.query(Key).first()
    #     current_key_value = current_key.key
    #     print(f"Current key value from database: {current_key_value}")
    # finally:
    #     db.close()
    try:
        current_key = db.query(Key).first()
        current_key_value = current_key.key
        machine_type, rotors, rotor_positions, ring_positions = get_rotor_settings_from_db(user_id, db)
        reflector_type = "B"  # This can also be dynamic if stored in the database
        print(f"Machine type: {machine_type}, Rotors: {rotors}, Rotor positions: {rotor_positions}, Ring positions: {ring_positions}, Reflector type: {reflector_type}")

        enigma_machine = Enigma(machine_type, rotors, rotor_positions, ring_positions, reflector_type)
        encrypted_key = enigma_machine.encrypt_message(current_key_value.upper())
        print(f"Encrypted key: {encrypted_key}")

        return {"encrypted_key": encrypted_key}  # Ensure this format
    except Exception as e:
        print(f"Exception: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))