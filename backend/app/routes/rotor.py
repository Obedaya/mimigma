from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal

router = APIRouter()

@router.get("/rotor", tags=["Rotor"])
def read_rotor_setting():
    db = SessionLocal()
    try:
        # Logic to set the rotor setting
        return {"message": "Rotor setting retrieved successfully"}
    finally:
        db.close()

@router.post("/rotor", tags=["Rotor"])
def update_rotor_setting():
    db = SessionLocal()
    try:
        # Logic to update the rotor setting in the database
        return {"setting": "Rotor setting updated successfully"}
    finally:
        db.close()