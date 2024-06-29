from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from ..database import get_db, SessionLocal
from ..models import Key, History
from sqlalchemy import desc
from ..enigma.enigma import Enigma
from ..enigma.rotor import get_rotor_settings_from_db
from ..crud import get_rotor_settings, get_reflector_settings

router = APIRouter()

@router.get("/lamp", tags=["Lamp"])
def get_encrypted_key(user_id: int):
    db = SessionLocal()
    try:
        current_key = db.query(Key).first()
        current_key_value = current_key.key
        rotor_settings = get_rotor_settings(db, user_id)
        reflector_settings = get_reflector_settings(db, user_id)
        
        machine_type = rotor_settings.machine_type
        rotors = rotor_settings.rotors
        rotor_positions = rotor_settings.rotor_positions
        ring_positions = rotor_settings.ring_positions
        reflector_type = reflector_settings.reflector
        plugboard = rotor_settings.plugboard
        
        print(f"Machine type: {machine_type}, Rotors: {rotors}, Rotor positions: {rotor_positions}, Ring positions: {ring_positions}, Reflector type: {reflector_type}, Plugboard: {plugboard}")

        enigma_machine = Enigma(machine_type, rotors, rotor_positions, ring_positions, reflector_type, user_id, plugboard)
        encrypted_key = enigma_machine.encrypt_message(current_key_value.upper())
        print(f"Encrypted key: {encrypted_key}")
        
        # latest_history = db.query(History).order_by(desc(History.id)).first()
        latest_history = db.query(History).filter(History.user_id == user_id).first()
        if latest_history:
            new_encrypted = latest_history.encrypted + encrypted_key
            plain = latest_history.plain
        else:
            new_encrypted = encrypted_key
            plain = ""

        if len(new_encrypted) > 120:
            new_encrypted = new_encrypted[-120:]

        if latest_history:
            latest_history.encrypted = new_encrypted
        else:
            new_history = History(user_id=user_id, plain=plain, encrypted=new_encrypted)
            db.add(new_history)

        
        db.commit()


        return {"encrypted_key": encrypted_key}
    except Exception as e:
        print(f"Exception: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
