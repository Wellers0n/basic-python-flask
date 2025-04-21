import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

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

def test_update_task():
  new_task = {
      "title": "Test Task",
      "description": "This is a test task."
  }
  response = requests.post(f"{BASE_URL}/tasks", json=new_task)
  task_id = response.json().get("task").get("id")
  
  updated_task = {
      "title": "Updated Task",
      "description": "This is an updated test task.",
      "completed": True
  }
  
  response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=updated_task)
  
  assert response.status_code == 200
  response_json = response.json()
  assert response_json.get("task").get("title") == updated_task["title"]
  
def test_delete_task():
  new_task = {
      "title": "Test Task",
      "description": "This is a test task."
  }
  response = requests.post(f"{BASE_URL}/tasks", json=new_task)
  task_id = response.json().get("task").get("id")
  
  response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
  
  assert response.status_code == 200
  response_json = response.json()
  assert response_json.get("message") == "Task deleted successfully!"