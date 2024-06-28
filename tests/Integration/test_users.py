# f"""rom backend.app.database import engine, check_db_connection
# from backend.app.init_db import init_db, sync_db_with_json, remove_user_from_db
# import pytest
# import json
# import requests
# import time
# from backend.app.add_user import add_default_test_user, delete_default_test_user
# from backend.app.config import file_path
#
# def get_users():
#     """Helper function to fetch users from the backend."""
#     try:
#         response = requests.get("http://backend:9000/users")
#         print("Users from backend:", response.json())
#     except Exception as e:
#         print(f"Error fetching users from backend: {e}")
#
# def read_users_from_json():
#     """Helper function to read users from the JSON file."""
#     try:
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#             print("Users from JSON:", data['users'])
#     except Exception as e:
#         print(f"Error reading from JSON file: {e}")
#
# @pytest.fixture(scope="function")
# def user_setup_and_teardown():
#     # print("Adding default test user now")
#     add_default_test_user()
#     check_db_connection(engine)
#     init_db()
#     sync_db_with_json()
#
#     # Allow time for the application to update and fetch current users
#     # time.sleep(5)
#     # get_users()
#     # read_users_from_json()
#
#     yield
#
#     # print("Removing default test user now")
#     delete_default_test_user()
#
#     remove_user_from_db("testuser")
#     # Allow time for the application to update and fetch current users
#     # time.sleep(5)
#     # get_users()
#     # read_users_from_json()
#
# def test_add_user(user_setup_and_teardown):
#     # print("Testing addition of user...")
#     user_exists = check_user_exists(file_path, "testuser")
#     # print(f"User existence check for 'add': {user_exists}")
#     assert user_exists == True, "User should exist after adding"
#
# def test_delete_user(user_setup_and_teardown):
#     # print("Testing deletion of user...")
#     delete_default_test_user()
#     # print("User deletion executed.")
#     user_exists = check_user_exists(file_path, "testuser")
#     # print(f"User existence check for 'delete': {user_exists}")
#     assert user_exists == False, "User should not exist after deletion"
#
# def check_user_exists(file_path, username):
#     print(f"Checking if user {username} exists in the file...")
#     try:
#         with open(file_path, "r") as file:
#             data = json.load(file)
#             for user in data["users"]:
#                 if user["username"] == username:
#                     print(f"User {username} found.")
#                     return True
#     except Exception as e:
#         print(f"An error occurred when checking user existence: {e}")
#     print(f"User {username} not found.")
#     return False
# """