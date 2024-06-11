from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import sessionmaker, Session

from ..schemas import RotorSettingCreate
from ..crud import get_rotor_settings
from ..database import get_db, SessionLocal, engine
from ..models import RotorSettings, Base


router = APIRouter()

Base.metadata.create_all(bind=engine)

"""
@router.get("/rotor/{user_id}", tags=["Rotor"], response_model=RotorSettings)
def read_rotor_setting(user_id: int, db: Session = Depends(get_db)):
    try:
        settings = get_rotor_settings(db, user_id=user_id)
        if settings is None:
            raise HTTPException(status_code=404, detail="Settings not found")
        return settings
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
"""

@router.post("/rotor", tags=["Rotor"])
async def update_rotor_setting(data: RotorSettingCreate):
    db = SessionLocal()
    try:
        existing_setting = db.query(RotorSettings).filter_by(user_id=data.user_id).first()

        if existing_setting:
            # Update existing record
            existing_setting.machine_type = data.machine_type
            existing_setting.rotors = data.rotors
            existing_setting.rotor_positions = data.rotor_positions
            existing_setting.ring_positions = data.ring_positions
            db.commit()
            db.refresh(existing_setting)
            message = "Rotor setting updated successfully"
        else:
            # Insert new record
            rotor_setting = RotorSettings(
                user_id=data.user_id,
                machine_type=data.machine_type,
                rotors=data.rotors,
                rotor_positions=data.rotor_positions,
                ring_positions=data.ring_positions
            )
            db.add(rotor_setting)
            db.commit()
            db.refresh(rotor_setting)
            message = "Rotor setting created successfully"

        print(f"User ID: {data.user_id}")
        print(f"Machine Type: {data.machine_type}")
        print(f"Rotors: {data.rotors}")
        print(f"Rotor Positions: {data.rotor_positions}")
        print(f"Ring Positions: {data.ring_positions}")

        return {"message": message}
    finally:
        db.close()

@router.post("/rotor/count", tags=["Rotor"])
async def rotor_count(count: int):
    db = SessionLocal()
    try:
        print(f"Rotor count: {count}")
        # Logic to count the number of rotors
        return {"message": "Rotor count retrieved successfully"}
    finally:
        db.close()

@router.get("/rotor/standard", tags=["Rotor"])
async def standard_rotor(variant: str):
    try:
        turnovers = {}
        if variant == "M1":
            turnovers = {"I": "Q", "II": "E", "III": "V", "IV": "J", "V": "Z"}
        elif variant == "M3":
            turnovers = {"I": "Q", "II": "E", "III": "V", "IV": "J", "V": "Z", "VI": "ZM", "VII": "ZM", "VIII": "ZM"}
        elif variant == "Norway":
            turnovers = {"I": "Q", "II": "E", "III": "V", "IV": "J", "V": "Z"}
        else:
            raise HTTPException(status_code=400, detail="Invalid variant")
        return {"turnovers": turnovers}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
