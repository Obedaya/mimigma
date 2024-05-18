import json
from .config import file_path

def add_user(file_path, name, username, email, password):
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
    add_user(file_path, "Test User", "testuser", "test@example.com", "password123")

def delete_user(file_path, username):
    try:
        with open(file_path, "r+") as file:
            data = json.load(file)
            # Filter out the user to delete
            data["users"] = [user for user in data["users"] if user["username"] != username]
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()  # Remove remaining part of old data
        print("User deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_default_test_user():
    delete_user(file_path, "testuser")

# if __name__ == '__main__':
#     delete_default_test_user()


