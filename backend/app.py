from flask import Flask, request, jsonify
from flask_cors import CORS
from Controller import TaskController

app = Flask(__name__)
CORS(app)

controller = TaskController()

@app.route('/tasks', methods=['GET'])
def get_tasks():
  tasks = controller.get_all_tasks()
  return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
  data = request.json
  task_type = data.get("type")
  title = data.get("title")
  description = data.get("description")
  frequency = data.get("frequency", None)  # Optional for recurring tasks
  try:
    task = controller.create_task(task_type, title, description, frequency)
    return jsonify(task.to_dict()), 201
  except ValueError as e:
    return jsonify({"error": str(e)}), 400

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
  controller.delete_task(task_id)
  return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
  app.run(debug=True)
