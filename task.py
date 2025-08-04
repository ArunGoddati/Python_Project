import uuid
from datetime import datetime

class Task:
    def __init__(self, title, priority, due_date, status="Pending", task_id=None):
        self.id = task_id if task_id else str(uuid.uuid4())[:8]
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            priority=data["priority"],
            due_date=data["due_date"],
            status=data["status"],
            task_id=data["id"]
        )
