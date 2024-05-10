from .database import SessionLocal, engine
from .models import Base, User
from .utils import hash_password, read_user_data

def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        user_data = read_user_data()
        # check if there are any users already
        if db.query(User).count() == 0:
            db.add_all([
                User(
                    name=user["name"],
                    username=user["username"],
                    email=user["email"],
                    password=hash_password(user["password"])
                    ) for user in user_data  
                ])
            db.commit()
    finally:
        db.close()

# Perform a sync of the JSON file and the db after adding a user
def sync_db_with_json():
    db = SessionLocal()
    try:
        user_data = read_user_data()
        existing_users = {user.username: user for user in db.query(User).all()}
        new_users = [
            User(
                name=user["name"],
                username=user["username"],
                email=user["email"],
                password=hash_password(user["password"])
            ) for user in user_data if user["username"] not in existing_users
        ]
        if new_users:
            db.add_all(new_users)
            db.commit()
    finally:
        db.close()


