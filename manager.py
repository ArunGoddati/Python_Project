import json
from datetime import datetime, timedelta
from task import Task

class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, title, priority, due_date):
        task = Task(title, priority, due_date)
        self.task_list.append(task)

    def view_tasks(self, filter_by=None, value=None):
        tasks = self.task_list

        if filter_by == "status":
            tasks = [t for t in tasks if t.status.lower() == value.lower()]
        elif filter_by == "due_date":
            today = datetime.today().date()
            if value == "today":
                tasks = [t for t in tasks if t.due_date == today.isoformat()]
            elif value == "week":
                week_later = today + timedelta(days=7)
                tasks = [t for t in tasks if today.isoformat() <= t.due_date <= week_later.isoformat()]

        if not tasks:
            print("No matching tasks found.")
        else:
            print("\nID        | Title           | Priority | Due Date   | Status")
            print("-" * 60)
            for task in tasks:
                print(f"{task.id:<10} | {task.title:<15} | {task.priority:<8} | {task.due_date} | {task.status}")

    def update_task(self, task_id):
        for task in self.task_list:
            if task.id == task_id:
                task.title = input("New Title (leave blank to skip): ") or task.title

                priority = input("New Priority (Low/Medium/High, leave blank to skip): ").capitalize()
                if priority in ["Low", "Medium", "High"]:
                    task.priority = priority

                due_date = input("New Due Date (YYYY-MM-DD, leave blank to skip): ")
                if due_date:
                    try:
                        datetime.strptime(due_date, "%Y-%m-%d")
                        task.due_date = due_date
                    except ValueError:
                        print("Skipping invalid date.")
                return True
        return False

    def mark_complete(self, task_id):
        for task in self.task_list:
            if task.id == task_id:
                task.status = "Completed"
                return True
        return False

    def delete_task(self, task_id):
        original_len = len(self.task_list)
        self.task_list = [t for t in self.task_list if t.id != task_id]
        return len(self.task_list) < original_len

    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump([task.to_dict() for task in self.task_list], f, indent=2)

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                tasks = json.load(f)
                self.task_list = [Task.from_dict(t) for t in tasks]
        except FileNotFoundError:
            self.task_list = []
