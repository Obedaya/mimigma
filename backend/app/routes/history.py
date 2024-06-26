from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from ..database import SessionLocal, get_db, engine
from ..models import Key, History

router = APIRouter()

@router.get("/history", tags=["History"])
def get_history():
    db = SessionLocal()
    try:
        # Logic to get the lamp status for the last pressed key
        latest_history = db.query(History).order_by(desc(History.id)).first()
        plain = latest_history.plain
        encrypted = latest_history.encrypted
        # print(f"\t\t\t\t\t\t\tDATABASE PLAINTEXT: {plain} \t\t\t\t\t\t\nDATABASE ENCTEXT: {encrypted}")
        return {"plain": plain, "encrypted": encrypted}
    finally:
        db.close()

@router.get("/deletehistory", tags=["History"])
def delete_history():
    db = SessionLocal();
    try:
        latest_history = db.query(History).order_by(desc(History.id)).first()
        if latest_history:
            new_history = History(plain="", encrypted="")
            db.add(new_history)
        db.commit()
        return {"message": "History cleared."}
    finally:
        db.close()

    

