from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal

router = APIRouter()

@router.get("/reflector", tags=["Reflector"])
def read_reflector_setting():
    db = SessionLocal()
    try:
        # Logic to set the reflector setting
        return {"message": "Reflector setting retrieved successfully"}
    finally:
        db.close()

@router.post("/reflector", tags=["Reflector"])
def update_reflector_setting():
    db = SessionLocal()
    try:
        # Logic to update the reflector setting in the database
        return {"setting": "Reflector setting updated successfully"}
    finally:
        db.close()