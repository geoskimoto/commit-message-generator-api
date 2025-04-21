class Task {
    constructor(name) {
        this.name = name;
        this.completed = false;
    }
}

class TaskManager {
    constructor() {
        this.tasks = [];
    }

    addTask(name) {
        const task = new Task(name);
        this.tasks.push(task);
    }

    getAllTasks() {
        return this.tasks;
    }
}
