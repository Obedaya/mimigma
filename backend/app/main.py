import asyncio
from fastapi import FastAPI
from .database import engine, check_db_connection
from .models import Base, User
from .utils import read_user_data, hash_password
from .add_test_user import add_default_test_user
from .routes import users, login, general, items
from .init_db import init_db, sync_db_with_json 
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
app.include_router(users.router)
app.include_router(login.router)
app.include_router(general.router)
app.include_router(items.router)

@app.on_event("startup")
async def startup_event():
    add_default_test_user()
    await asyncio.sleep(1)
    check_db_connection(engine)
    init_db()
    sync_db_with_json()
