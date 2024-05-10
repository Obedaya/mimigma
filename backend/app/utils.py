import json, hashlib, logging

def read_user_data():
    try:
        with open("app/users_config.json", "r") as file:
            data = json.load(file)
        return data["users"]
    except FileNotFoundError:
        logging.error("File not found: users_config.json")
        return []
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the file")
        return []

# Stephane : hash fonction SHA256
def hash_password(password: str) -> str:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
