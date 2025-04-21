from flask import Flask, request, jsonify
from models.task import Task

tasks = []

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Welcome to the Task Manager API!"
      
    @app.route('/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()
        new_task = Task(id=len(tasks) + 1, title=data['title'], description=data.get('description', ''))
        tasks.append(new_task)
        print(f"Task created: {new_task}")
        return jsonify({"message": "Task created successfully!", "task": new_task.to_dict()}), 201
      
    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        return jsonify([task.to_dict() for task in tasks]), 200
      
    @app.route('/tasks/<int:task_id>', methods=['GET'])
    def get_task(task_id):
        task = next((task for task in tasks if task.id == task_id), None)
        if task:
            return jsonify(task.to_dict()), 200
        return jsonify({"message": "Task not found!"}), 404
    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        data = request.get_json()
        task = next((task for task in tasks if task.id == task_id), None)
        if task:
            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            task.completed = data.get('completed', task.completed)
            return jsonify({"message": "Task updated successfully!", "task": task.to_dict()}), 200
        return jsonify({"message": "Task not found!"}), 404

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        global tasks
        tasks = [task for task in tasks if task.id != task_id]
        return jsonify({"message": "Task deleted successfully!"}), 200
      
    @app.route('/tasks/<int:task_id>/complete', methods=['POST'])
    def complete_task(task_id):
        task = next((task for task in tasks if task.id == task_id), None)
        if task:
            task.completed = True
            return jsonify({"message": "Task marked as completed!", "task": task.to_dict()}), 200
        return jsonify({"message": "Task not found!"}), 404

    app.run(debug=True)