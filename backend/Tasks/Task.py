class Task:
  def __init__(self, task_id, title, description):
    self.task_id = task_id
    self.title = title
    self.description = description

  def to_dict(self):
    """Convert task to a dictionary format."""  
    return {
      "id": self.task_id,
      "title": self.title,
      "description": self.description,
    }
