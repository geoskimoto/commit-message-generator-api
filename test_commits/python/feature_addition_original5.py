class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_complete(self):
        self.completed = True

class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(Task(name))

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

class ProjectManager:
    def __init__(self):
        self.projects = []

    def add_project(self, title):
        self.projects.append(Project(title))

    def get_all_projects(self):
        return self.projects
