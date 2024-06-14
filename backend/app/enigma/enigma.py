from fastapi import FastAPI, APIRouter, HTTPException, Depends
from pydantic import BaseModel
from .rotor import RotorMachine, get_rotor_settings_from_db
from .reflector import Reflector
from ..database import SessionLocal  # Import SessionLocal
from ..models import Key, RotorSettings
from sqlalchemy.orm import Session

router = APIRouter()

class KeyInput(BaseModel):
    key: str

class Enigma:
    def __init__(self, machine_type, rotors, rotor_positions, ring_positions, reflector_type):
        self.rotor_machine = RotorMachine(machine_type, rotors, rotor_positions, ring_positions)
        self.reflector = Reflector(reflector_type)
        self.db = SessionLocal()  # Initialize a session

    def update_rotor_positions_in_db(self):
        user_id = self.db.query(RotorSettings.user_id).first()[0]
        updated_positions = "".join(chr(pos + ord('A')) for pos in self.rotor_machine.rotor_positions)
        db_rotor_settings = self.db.query(RotorSettings).filter(RotorSettings.user_id == user_id).first()
        if db_rotor_settings:
            db_rotor_settings.rotor_positions = updated_positions
            self.db.commit()

    def enigma_encrypt(self, key):
        print(f"Encrypting letter: {key}")
        # Advance rotors
        self.rotor_machine.advance_rotors()
        print(f"Rotor positions after advancement: {self.rotor_machine.rotor_positions}")
        # Update rotor positions in the database
        self.update_rotor_positions_in_db()
        # Encrypt through rotors forward
        encrypted_letter = self.rotor_machine.encrypt_letter(key)
        print(f"Letter after forward encryption: {encrypted_letter}")
        # Reflect
        reflected_letter = self.reflector.encrypt(encrypted_letter)
        print(f"Letter after reflection: {reflected_letter}")
        # Encrypt through rotors in reverse
        final_letter = self.rotor_machine.encrypt_letter_reverse(reflected_letter)
        print(f"Letter after backward encryption: {final_letter}")
        
        return final_letter
    
    def encrypt_message(self, key):
        return self.enigma_encrypt(key)
