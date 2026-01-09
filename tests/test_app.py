import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

import json

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
def test_update_task():
    client = app.test_client()
    client.post(
        "/tasks",
        data=json.dumps({"title": "Task to update"}),
        content_type="application/json"
    )

    res = client.put("/tasks/1")
    assert res.status_code == 200
    assert res.json["completed"] is True
def test_delete_task():
    client = app.test_client()
    client.post(
        "/tasks",
        data=json.dumps({"title": "Task to delete"}),
        content_type="application/json"
    )

    res = client.delete("/tasks/1")
    assert res.status_code == 204
