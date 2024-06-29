import pytest
import requests

BASE_URL = "http://backend:9000"

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL


def test_login_success(base_url):
    response = requests.post(f"{base_url}/login?username=user_test_2&password=password100")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert data["message"] == "Login successful"
    assert "user" in data
    assert "access_token" in data


def test_login_failure(base_url):
    response = requests.post(f"{base_url}/login?username=user_test_2&password=wrongpassword")
    assert response.status_code == 401

    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Invalid username or password"
