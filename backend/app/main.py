from fastapi import FastAPI
from .database import engine, check_db_connection
from .models import Base, User
from .utils import read_user_data, hash_password
from .routes import users, login, general, items
from .init_db import init_db 

app = FastAPI()

#include routes in the app
app.include_router(users.router)
app.include_router(login.router)
app.include_router(general.router)
app.include_router(items.router)

@app.on_event("startup")
async def startup_event():
    check_db_connection(engine)
    init_db()
