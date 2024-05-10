from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal

router = APIRouter()

@router.get("/lamp", tags=["Lamp"])
def get_lamp():
    db = SessionLocal()
    try:
        # Logic to get the lamp status for the last pressed key
        return {"status": "Lamp is on"}
    finally:
        db.close()