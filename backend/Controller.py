from Model import TaskModel

class TaskController:
  def __init__(self):
    self.model = TaskModel()

  def create_task(self, task_type, title, description, frequency=None):
    """Handle task creation."""
    return self.model.create_task(task_type, title, description, frequency)

  def get_all_tasks(self):
    """Handle fetching all tasks."""
    return self.model.get_tasks()

  def delete_task(self, task_id):
    """Handle deleting a task."""
    self.model.delete_task(task_id)
