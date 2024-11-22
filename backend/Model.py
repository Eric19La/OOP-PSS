from Tasks.AntiTask import AntiTask
from Tasks.RecurringTask import RecurringTask
from Tasks.TransientTask import TransientTask

class TaskModel:
  def __init__(self):
    self.tasks = []
    self.task_id_counter = 1

  def create_task(self, task_type, title, description, frequency=None):
    """Create a task and add it to the task list."""
    if task_type == "anti":
        task = AntiTask(self.task_id_counter, title, description)
    elif task_type == "recurring":
        task = RecurringTask(self.task_id_counter, title, description, frequency)
    elif task_type == "transient":
        task = TransientTask(self.task_id_counter, title, description)
    else:
        raise ValueError("Invalid task type")

    self.tasks.append(task)
    self.task_id_counter += 1
    return task

  def get_tasks(self):
    """Retrieve all tasks."""
    return [task.to_dict() for task in self.tasks]

  def delete_task(self, task_id):
    """Delete a task by its ID."""
    self.tasks = [task for task in self.tasks if task.task_id != task_id]
