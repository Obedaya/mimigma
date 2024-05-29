from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
# from app.enigma.enigma import Enigma
from sqlalchemy.orm import Session
from ..database import SessionLocal

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

@router.post("/keyboard", tags=["Keyboard"])
def get_encrypted_key(input: KeyInput):
    global last_encrypted_key
    try:
        # dummy 
        encrypted_key = dummy_encrypt(input.key)
        last_encrypted_key = encrypted_key
        
        # enigma
        # encrypted_key = enigma_machine.encrypt(input.key.upper())
        # last_encrypted_key = encrypted_key
        
        return {"encrypted_key": encrypted_key}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/lamp", tags=["Lamp"])
def get_lamp():
    global last_encrypted_key
    try:
        if last_encrypted_key:
            return {"status": f"Lamp is on for {last_encrypted_key}"}
        else:
            return {"status": "No key has been encrypted yet."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
