from pydantic import BaseModel
from typing import List

class RotorSettingCreate(BaseModel):
    user_id: str
    machine_type: str
    rotors: List[str]
    rotor_positions: str
    ring_positions: str
    plugboard: List[List[str]]

    class Config:
        orm_mode = True

class ReflectorSettingCreate(BaseModel):
    user_id: int
    reflector: str

    class Config:
        orm_mode = True

class PlugboardSettingCreate(BaseModel):
    user_id: int
    plugboard: List[List[str]]

    class Config:
        orm_mode = True