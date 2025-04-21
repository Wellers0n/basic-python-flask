import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"
tasks = [] 

def test_create_task():
  new_task = {
      "title": "Test Task",
      "description": "This is a test task."
  }
  response = requests.post(f"{BASE_URL}/tasks", json=new_task)
  
  assert response.status_code == 201
  response_json = response.json()
  assert "message" in response_json
  assert "id" in response_json.get("task")
  
def test_get_tasks():
  response = requests.get(f"{BASE_URL}/tasks")
  
  assert response.status_code == 200
  response_json = response.json()
  assert isinstance(response_json, list)
  if len(response_json) > 0:
      assert "id" in response_json[0]
      assert "title" in response_json[0]
      assert "description" in response_json[0]
      assert "completed" in response_json[0]
  