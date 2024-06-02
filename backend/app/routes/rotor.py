from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from schemas import RotorSettings, RotorSettingsCreate
from crud import get_rotor_settings, create_or_update_rotor_settings
from ..database import get_db

router = APIRouter()

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

@router.post("/rotor", tags=["Rotor"], response_model=RotorSettings)
def update_rotor_setting(settings: RotorSettingsCreate, db: Session = Depends(get_db)):
    try:
        db_settings = create_or_update_rotor_settings(db=db, settings=settings)
        return db_settings
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

