from datetime import datetime

class Task:
    def __init__(self, name, estimated_hours=0, deadline=None):
        self.name = name
        self.completed = False
        self.estimated_hours = estimated_hours
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None
        self.completed_at = None

    def mark_complete(self):
        self.completed = True
        self.completed_at = datetime.now()

    def is_overdue(self):
        return self.deadline and not self.completed and datetime.now() > self.deadline

class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, name, estimated_hours=0, deadline=None):
        self.tasks.append(Task(name, estimated_hours, deadline))

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def get_progress(self):
        total = len(self.tasks)
        completed = len(self.get_completed_tasks())
        return round((completed / total) * 100) if total > 0 else 0

class ProjectManager:
    def __init__(self):
        self.projects = []

    def add_project(self, title):
        self.projects.append(Project(title))

    def get_all_projects(self):
        return self.projects

    def get_overall_progress(self):
        if not self.projects:
            return 0
        return round(sum(p.get_progress() for p in self.projects) / len(self.projects))
