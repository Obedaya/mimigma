import json
from .utils import hash_password

def add_test_user(file_path, name, username, email, password):
    test_user = {
        "name": name,
        "username": username,
        "email": email,
        "password": password
    }
    try:
        with open(file_path, "r+") as file:
            data = json.load(file)
            data["users"].append(test_user)
            # Reset file position to the beginning
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()  # Remove remaining part of old data
        print("Test user added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_default_test_user():
    config_path = "app/users_config.json"
    add_test_user(config_path, "Test User", "testuser", "test@example.com", "password123")

if __name__ == '__main__':
    add_default_test_user()


