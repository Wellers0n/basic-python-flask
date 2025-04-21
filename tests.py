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
  