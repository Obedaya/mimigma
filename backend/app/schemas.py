from pydantic import BaseModel
from typing import List

class RotorSettingCreate(BaseModel):
    user_id: str
    machine_type: str
    rotors: List[int]
    rotor_positions: List[int]
    ring_positions: List[int]

    class Config:
        orm_mode = True
