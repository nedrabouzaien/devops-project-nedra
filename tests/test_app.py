import json
from app import app

def test_health():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

def test_create_task():
    client = app.test_client()
    res = client.post(
        "/tasks",
        data=json.dumps({"title": "Test task"}),
        content_type="application/json"
    )
    assert res.status_code == 201
    assert res.json["title"] == "Test task"

def test_get_tasks():
    client = app.test_client()
    res = client.get("/tasks")
    assert res.status_code == 200
