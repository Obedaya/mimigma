import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    client = TestClient(app)
    return client

def test_app_startup_and_routes(client):
    # Test, ob die Anwendung erfolgreich startet
    response = client.get("/")
    assert response.status_code == 200

    headers = {
        "Origin": "http://localhost:8080",
        "Access-Control-Request-Method": "GET",
    }
    response = client.options("/", headers=headers)
    assert response.status_code == 200
    assert "Access-Control-Allow-Origin" in response.headers

    routes = ["/users", "/login", "/rotor", "/plugboard", "/lamp", "/reflector", "/keyboard", "/settings", "/history"]
    for route in routes:
        response = client.get(route)
        assert response.status_code != 404, f"Route {route} nicht gefunden"

