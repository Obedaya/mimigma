from fastapi import FastAPI
from .database import engine, check_db_connection
from .models import Base, User
from .utils import read_user_data, hash_password
from .routes import users, login, general, items, rotor, ring, plugboard, lamp, reflector
from .init_db import init_db 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:5173",
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
app.include_router(items.router)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(rotor.router)
app.include_router(ring.router)
app.include_router(plugboard.router)
app.include_router(lamp.router)
app.include_router(reflector.router)

@app.on_event("startup")
async def startup_event():
    check_db_connection(engine)
    init_db()
