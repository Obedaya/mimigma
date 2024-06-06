from pydantic import BaseModel
from typing import List

class RotorSettingCreate(BaseModel):
    user_id: str
    machine_type: str
    rotors: List[str]
    rotor_positions: str
    ring_positions: str

    class Config:
        orm_mode = True
