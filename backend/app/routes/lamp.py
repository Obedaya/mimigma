from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
# from app.enigma.enigma import Enigma
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Key

router = APIRouter()

class KeyInput(BaseModel):
    key: str

# example
# enigma_machine = Enigma(
#     rotors=['I', 'II', 'III'],
#     reflector='B',
#     ring_settings=[1, 1, 1],
#     plugboard_settings={'A': 'B', 'C': 'D'}
# )

last_encrypted_key = None

# dummy caesar
def dummy_encrypt(key: str) -> str:
    if not key.isalpha() or len(key) != 1:
        raise ValueError("Invalid key")
    return chr((ord(key.upper()) - 65 + 3) % 26 + 65)

@router.get("/lamp", tags=["Lamp"])
def get_encrypted_key():
    db = SessionLocal()
    try:
        # Logic to get the lamp status for the last pressed key
        current_key = db.query(Key).first()
        current_key_value = current_key.key
    finally:
        db.close()
    try:
        # dummy 
        encrypted_key = dummy_encrypt(current_key_value)
        print(encrypted_key)
        
        # enigma
        # encrypted_key = enigma_machine.encrypt(input.key.upper())
        # last_encrypted_key = encrypted_key
        
        return {"encrypted_key": encrypted_key}  # Ensure this format
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))