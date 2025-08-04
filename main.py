from manager import TaskManager
from datetime import datetime

tm = TaskManager()
tm.load_from_file()

def validate_priority(p):
    return p.capitalize() in ["Low", "Medium", "High"]

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def menu():
    print("""
TaskForge – Terminal Task Manager

1. Add Task
2. View All Tasks
3. View by Status
4. View by Due Date
5. Update Task
6. Mark as Complete
7. Delete Task
8. Save & Exit
""")

while True:
    menu()
    choice = input("Enter choice (1-8): ").strip()

    if choice == "1":
        title = input("Title: ").strip()
        
        priority = input("Priority (Low/Medium/High): ").capitalize()
        while not validate_priority(priority):
            priority = input("Invalid. Enter Priority (Low/Medium/High): ").capitalize()
        
        due_date = input("Due Date (YYYY-MM-DD): ").strip()
        while not validate_date(due_date):
            due_date = input("Invalid. Enter valid date (YYYY-MM-DD): ").strip()

        tm.add_task(title, priority, due_date)

    elif choice == "2":
        tm.view_tasks()

    elif choice == "3":
        status = input("Enter status (Pending/Completed): ").capitalize()
        while status not in ["Pending", "Completed"]:
            status = input("Invalid. Enter 'Pending' or 'Completed': ").capitalize()
        tm.view_tasks(filter_by="status", value=status)

    elif choice == "4":
        time_filter = input("Enter due date filter (today/week): ").lower()
        while time_filter not in ["today", "week"]:
            time_filter = input("Invalid. Choose 'today' or 'week': ").lower()
        tm.view_tasks(filter_by="due_date", value=time_filter)

    elif choice == "5":
        task_id = input("Enter Task ID to update: ").strip()
        if not tm.update_task(task_id):
            print("Task ID not found.")

    elif choice == "6":
        task_id = input("Enter Task ID to mark complete: ").strip()
        if not tm.mark_complete(task_id):
            print("Task ID not found.")

    elif choice == "7":
        task_id = input("Enter Task ID to delete: ").strip()
        if not tm.delete_task(task_id):
            print("Task ID not found.")

    elif choice == "8":
        tm.save_to_file()
        print("Tasks saved. Exiting...")
        break

    else:
        print("Invalid choice. Enter a number from 1 to 8.")
