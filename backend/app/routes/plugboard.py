from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal

router = APIRouter()

@router.get("/plugboard", tags=["Plugboard"])
def read_plugboard_setting():
    db = SessionLocal()
    try:
        # Logic to set the plugboard setting
        return {"message": "Plugboard setting retrieved successfully"}
    finally:
        db.close()

@router.post("/plugboard", tags=["Plugboard"])
def update_plugboard_setting():
    db = SessionLocal()
    try:
        # Logic to update the plugboard setting in the database
        return {"setting": "Plugboard setting updated successfully"}
    finally:
        db.close()