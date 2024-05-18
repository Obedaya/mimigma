import os

DATABASE_URL = os.getenv("DATABASE_URL")

# path to the JSON file
file_path = 'app/users_config.json'

user_data = {
    "name": "E2E",
    "username": "Etest",
    "email": "etest@test.com",
    "password": "etest"
}

