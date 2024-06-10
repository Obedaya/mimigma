from fastapi import FastAPI, APIRouter, HTTPException, Depends
from pydantic import BaseModel
from .rotor import RotorMachine, get_rotor_settings_from_db
from .reflector import Reflector
from ..database import get_db, SessionLocal
from ..models import Key
from sqlalchemy.orm import Session

router = APIRouter()

class KeyInput(BaseModel):
    key: str

class Enigma:
    def __init__(self, machine_type, rotors, rotor_positions, ring_positions, reflector_type):
        self.rotor_machine = RotorMachine(machine_type, rotors, rotor_positions, ring_positions)
        self.reflector = Reflector(reflector_type)
    
    def enigma_encrypt(self, key):
        print(f"Encrypting letter: {key}")
        # Advance rotors
        self.rotor_machine.advance_rotors()
        print(f"Rotor positions after advancement: {self.rotor_machine.rotor_positions}")
        # Encrypt through rotors forward
        encrypted_letter = self.rotor_machine.encrypt_letter(key)
        print(f"Letter after forward encryption: {encrypted_letter}")
        # Reflect
        reflected_letter = self.reflector.encrypt(encrypted_letter)
        print(f"Letter after reflection: {reflected_letter}")
        # Encrypt through rotors in reverse
        final_letter = self.rotor_machine.encrypt_letter_reverse(reflected_letter)
        print(f"Final encrypted letter: {final_letter}")
        return final_letter
    
    def encrypt_message(self, key):
        return self.enigma_encrypt(key)