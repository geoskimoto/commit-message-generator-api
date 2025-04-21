class Task {
    constructor(name, estimatedHours = 0, deadline = null) {
        this.name = name;
        this.completed = false;
        this.estimatedHours = estimatedHours;
        this.deadline = deadline ? new Date(deadline) : null;
        this.completedAt = null;
    }

    markComplete() {
        this.completed = true;
        this.completedAt = new Date();
    }

    isOverdue() {
        if (!this.completed && this.deadline) {
            return new Date() > this.deadline;
        }
        return false;
    }
}

class Project {
    constructor(title) {
        this.title = title;
        this.tasks = [];
    }

    addTask(name, estimatedHours = 0, deadline = null) {
        this.tasks.push(new Task(name, estimatedHours, deadline));
    }

    getCompletedTasks() {
        return this.tasks.filter(task => task.completed);
    }

    getProgress() {
        const total = this.tasks.length;
        const completed = this.getCompletedTasks().length;
        return total === 0 ? 0 : Math.round((completed / total) * 100);
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

    getOverallProgress() {
        const projectProgress = this.projects.map(p => p.getProgress());
        if (projectProgress.length === 0) return 0;
        return Math.round(projectProgress.reduce((a, b) => a + b, 0) / projectProgress.length);
    }
}
