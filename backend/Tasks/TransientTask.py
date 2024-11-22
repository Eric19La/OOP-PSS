from .Task import Task

class TransientTask(Task):
  def __init__(self, task_id, title, description):
    super().__init__(task_id, title, description)
    self.type = "transient"

  def to_dict(self):
    task_dict = super().to_dict()
    task_dict["type"] = self.type
    return task_dict
