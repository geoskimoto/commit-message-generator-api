class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        task = Task(name)
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks
