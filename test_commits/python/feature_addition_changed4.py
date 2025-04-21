from datetime import datetime

class Task:
    def __init__(self, name, priority="normal"):
        self.name = name
        self.completed = False
        self.created_at = datetime.now()
        self.priority = priority
        self.completed_at = None

    def mark_complete(self):
        self.completed = True
        self.completed_at = datetime.now()

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority="normal"):
        task = Task(name, priority)
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]
