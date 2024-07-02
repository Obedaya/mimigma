import asyncio
from fastapi import FastAPI
from .database import engine, check_db_connection
from .routes import users, login, general, rotor, plugboard, lamp, reflector, keyboard, settings, history
from .init_db import init_db, sync_db_with_json
from fastapi.middleware.cors import CORSMiddleware
from app.enigma.enigma import Enigma

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://backend:9000",
    "http://localhost",
    "http://frontend:8080",
    "http://localhost:9000",
    "http://frontend:8081",
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#include routes in the app
app.include_router(general.router)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(rotor.router)
app.include_router(plugboard.router)
app.include_router(lamp.router)
app.include_router(reflector.router)
app.include_router(keyboard.router)
app.include_router(settings.router)
app.include_router(history.router)

@app.on_event("startup")
async def startup_event():
    await asyncio.sleep(1)
    check_db_connection(engine)
    init_db()
    sync_db_with_json()
