class Task {
    constructor(name, priority = 'normal') {
        this.name = name;
        this.completed = false;
        this.createdAt = new Date();
        this.priority = priority;
        this.completedAt = null;
    }

    markComplete() {
        this.completed = true;
        this.completedAt = new Date();
    }
}

class TaskManager {
    constructor() {
        this.tasks = [];
    }

    addTask(name, priority) {
        const task = new Task(name, priority);
        this.tasks.push(task);
    }

    getAllTasks() {
        return this.tasks;
    }

    getCompletedTasks() {
        return this.tasks.filter(task => task.completed);
    }

    getTasksByPriority(priority) {
        return this.tasks.filter(task => task.priority === priority);
    }
}
