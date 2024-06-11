from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import JSON

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Key(Base):
    __tablename__ = "keys"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, index=True)

class RotorSettings(Base):
    __tablename__ = "rotor_settings"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, unique=True, index=True)
    machine_type = Column(String, index=True)
    rotors = Column(JSON)
    rotor_positions = Column(String)
    ring_positions = Column(String)


class ReflectorSettings(Base):
    __tablename__ = "reflector_settings"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, unique=True, index=True)
    reflector = Column(String)
