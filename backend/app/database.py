from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL
import time

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# check if database is connected
def check_db_connection(engine):
    while True:
        try:
            # try to connect the db
            with engine.connect() as conn:
                # when the connection is successful, break the loop
                print("Database connection successful")
                break
        except Exception as e:
            print("Waiting for database connection...")
            print(e)
            # wait 2 seconds before connecting again
            time.sleep(2)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()