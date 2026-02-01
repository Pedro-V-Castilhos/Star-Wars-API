from fastapi.testclient import TestClient
from app.main import app

def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"greetings": "May the Force be with you!"}