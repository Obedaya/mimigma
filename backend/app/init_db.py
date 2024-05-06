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

