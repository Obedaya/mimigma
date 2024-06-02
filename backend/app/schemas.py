from pydantic import BaseModel
from typing import List

class RotorSettingsBase(BaseModel):
    user_id: int
    machine_type: str
    rotors: List[str]
    rotor_positions: str
    ring_positions: str

class RotorSettingsCreate(RotorSettingsBase):
    pass

class RotorSettings(RotorSettingsBase):
    id: int

    class Config:
        orm_mode = True
