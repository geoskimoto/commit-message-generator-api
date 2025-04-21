class TaskManager {
    constructor() {
        this.tasks = [];
    }

    addTask(name) {
        this.tasks.push({ name, completed: false });
    }
}

const manager = new TaskManager();
manager.addTask("Finish report");
