from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from ..database import SessionLocal, get_db, engine
from ..models import Key, History

router = APIRouter()

@router.post("/keyboard", tags=["Keyboard"])
def post_keyboard(key: str):
    db = SessionLocal()
    try:
        db.query(Key).delete()
        db.add(Key(key=key))
        db.commit()
        
        latest_history = db.query(History).order_by(desc(History.id)).first()
        if latest_history:
            new_plain = latest_history.plain + key
            encrypted = latest_history.encrypted
        else:
            new_plain = key
            encrypted = ""

        # Truncate the plain text if it exceeds 120 characters
        if len(new_plain) > 120:
            new_plain = new_plain[-120:]

        # Update the History entry or create a new one
        if latest_history:
            latest_history.plain = new_plain
        else:
            new_history = History(plain=new_plain, encrypted=encrypted)
            db.add(new_history)

        print(f"\t\t\t\t\tdatabase plain: {new_plain}")
        
        db.commit()
        # db.add(History(plain=))
        # plain = db.query(History).filter_by(user_id=user_id).first()
        # try:
        #     plaintext = db.query(History).filter_by(user_id=user_id).first()
        #     if (plaintext.len < 120):
        #         plaintext.plain = key + plaintext.plain
        #     else:
        #         plaintext.plain = key + plaintext.plain[:119]

        # # plain = db.execute(select(History).order_by(History.plain))
        # print(f"plain key: {plaintext.plain}")
        # TODO history add and remove

        # return {"status": "Key pressed: " + key}
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
