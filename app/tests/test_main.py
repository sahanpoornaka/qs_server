from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_check():
    response = client.get("/check/")
    assert response.status_code == 200
