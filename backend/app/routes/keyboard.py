from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Key

router = APIRouter()

@router.post("/keyboard/{key}", tags=["Keyboard"])
def post_keyboard(key: str):
    db = SessionLocal()
    try:
        db.query(Key).delete()
        db.add(Key(key=key))
        db.commit()

        return {"status": "Key pressed: " + key}
    finally:
        db.close()

@router.get("/keyboard", tags=["Keyboard"])
def get_keyboard():
    db = SessionLocal()
    try:
        # Logic to get the lamp status for the last pressed key
        current_key = db.query(Key).first()
        return {"key": current_key}
    finally:
        db.close()