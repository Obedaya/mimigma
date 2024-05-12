import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

file_path = '../../app/users_config.json'

user_data = {
    "name": "E2E",
    "username": "Etest",
    "email": "etest@test.com",
    "password": "etest"  
}

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

def login_via_webpage():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://localhost:8080")  
    time.sleep(2)  

    # Find elements and interact
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(user_data['username'])

    password_input = driver.find_element(By.ID, "passwort")  
    password_input.send_keys(user_data['password'])

    login_button = driver.find_element(By.CLASS_NAME, "login-button")
    login_button.click()

    # Check results
    time.sleep(2)
    try:
        driver.find_element(By.CLASS_NAME, "roter_panel")
        print("Login successful: 'roter_panel' found.")
    except:
        print("Login attempt failed: 'roter_panel' not found.")
    driver.quit()

if __name__ == '__main__':
    add_default_test_user()
    login_via_webpage()


