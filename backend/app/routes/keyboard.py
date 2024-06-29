from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from ..database import SessionLocal, get_db, engine
from ..models import Key, History

router = APIRouter()

@router.post("/keyboard", tags=["Keyboard"])
def post_keyboard(key: str, user_id: int):
    db = SessionLocal()
    try:
        db.query(Key).delete()
        db.add(Key(key=key))
        db.commit()
        
        # latest_history = db.query(History).order_by(desc(History.id)).first()
        latest_history = db.query(History).filter(History.user_id == user_id).first()
        if latest_history:
            new_plain = latest_history.plain + key
            encrypted = latest_history.encrypted
        else:
            new_plain = key
            encrypted = ""

        if len(new_plain) > 120:
            new_plain = new_plain[-120:]

        if latest_history:
            latest_history.plain = new_plain
        else:
            new_history = History(user_id=user_id, plain=new_plain, encrypted=encrypted)
            db.add(new_history)

        db.commit()
        
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
