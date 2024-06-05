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
async def update_rotor_setting(data: dict = Body(...)):
    db = SessionLocal()
    try:
        user_id = data["user_id"]
        machine_type = data["machine_type"]
        rotors = data["rotors"]
        rotor_positions = data["rotor_positions"]
        ring_positions = data["ring_positions"]
        # Logic to update the rotor setting in the database
        rotor_setting = RotorSettings(
            user_id=user_id,
            machine_type=machine_type,
            rotors=rotors,
            rotor_positions=rotor_positions,
            ring_positions=ring_positions
        )

        db.add(rotor_setting)
        db.commit()
        db.refresh(rotor_setting)

        print(f"User ID: {user_id}")
        print(f"Machine Type: {machine_type}")
        print(f"Rotors: {rotors}")
        print(f"Rotor Positions: {rotor_positions}")
        print(f"Ring Positions: {ring_positions}")

        return {"message": "Rotor setting updated successfully"}
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