class Task {
    constructor(name) {
        this.name = name;
        this.completed = false;
    }

    markComplete() {
        this.completed = true;
    }
}

class Project {
    constructor(title) {
        this.title = title;
        this.tasks = [];
    }

    addTask(name) {
        this.tasks.push(new Task(name));
    }

    getCompletedTasks() {
        return this.tasks.filter(task => task.completed);
    }
}

class ProjectManager {
    constructor() {
        this.projects = [];
    }

    addProject(title) {
        this.projects.push(new Project(title));
    }

    getAllProjects() {
        return this.projects;
    }
}
