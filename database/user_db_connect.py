import json
import psycopg2
import hashlib


def connect_to_postgresql():
    try:
        connection = psycopg2.connect(
            dbname="enigma_db",
            user="db_user",
            password="db_pass",
            host="l80c12f7bd5af",
            port="5432"
        )
        return connection
    except Exception as e:
        print("Error connecting to PostgreSQL:", e)
        return None


def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def insert_users(users):
    try:
        connection = connect_to_postgresql()
        if connection is not None:
            cursor = connection.cursor()
            for user in users:
                hashed_password = hash_password(user["password"])
                cursor.execute(
                    "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                    (user["username"], hashed_password, user["email"])
                )
            connection.commit()
            print("Users successfully inserted into the PostgreSQL database")
            cursor.close()
            connection.close()
    except Exception as e:
        print("Error inserting users into PostgreSQL:", e)

# Read JSON file
def read_json_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data["users"]
    except Exception as e:
        print("Error reading JSON file:", e)
        return []


if __name__ == "__main__":
    json_file = "user_config.json"
    users = read_json_file(json_file)
    if users:
        insert_users(users)
