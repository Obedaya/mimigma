from fastapi import APIRouter, HTTPException, Body
from sqlalchemy.orm import Session
from ..database import SessionLocal

router = APIRouter()

@router.get("/rotor", tags=["Rotor"])
def read_rotor_setting():
    db = SessionLocal()
    try:
        # Logic to set the rotor setting
        return {"message": "Rotor setting retrieved successfully"}
    finally:
        db.close()

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