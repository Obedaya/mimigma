from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from ..database import SessionLocal, get_db, engine
from ..models import Key, History

router = APIRouter()

@router.get("/history", tags=["History"])
def get_history(user_id: int):
    db = SessionLocal()
    try:
        # latest_history = db.query(History).order_by(desc(History.id)).first()
        latest_history = db.query(History).filter(History.user_id == user_id).first()

        if latest_history:
            plain = latest_history.plain
            encrypted = latest_history.encrypted
        else:
            plain = ""
            encrypted = ""
            new_history = History(user_id=user_id, plain=plain, encrypted=encrypted)
            db.add(new_history)

        return {"plain": plain, "encrypted": encrypted}
    finally:
        db.close()

@router.get("/deletehistory", tags=["History"])
def delete_history(user_id: int):
    db = SessionLocal()
    try:
        # latest_history = db.query(History).order_by(desc(History.id)).first()
        latest_history = db.query(History).filter(History.user_id == user_id).first()
        if latest_history:
            new_history = History(plain="", encrypted="")
            db.add(new_history)
        db.commit()
        return {"message": "History cleared."}
    finally:
        db.close()

    

