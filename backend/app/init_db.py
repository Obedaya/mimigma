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

def remove_user_from_db(username):
    db = SessionLocal()
    try:
        # Fetch the user to be deleted by username
        user_to_delete = db.query(User).filter(User.username == username).first()
        if user_to_delete:
            db.delete(user_to_delete)
            db.commit()
            print(f"User {username} removed from the database.")
        else:
            print(f"User {username} not found in the database.")
    except Exception as e:
        print(f"Error removing user {username} from the database: {e}")
    finally:
        db.close()

