from .Task import Task

class RecurringTask(Task):
  def __init__(self, task_id, title, description, frequency):
    super().__init__(task_id, title, description)
    self.type = "recurring"
    self.frequency = frequency  # e.g., "daily", "weekly"

  def to_dict(self):
    task_dict = super().to_dict()
    task_dict["type"] = self.type
    task_dict["frequency"] = self.frequency
    return task_dict
