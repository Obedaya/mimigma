import json, hashlib

def read_user_data():
    with open("app/users_config.json", "r") as file:
        data = json.load(file)
    return data["users"]

# Stephane : hash fonction SHA256
def hash_password(password: str) -> str:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
