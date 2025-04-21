class Task {
    constructor(name, priority = "normal", deadline = null) {
        this.name = name.trim();
        this.priority = priority;
        this.deadline = deadline;
        this.completed = false;
        this.createdAt = new Date().toISOString();
    }

    isOverdue() {
        if (!this.deadline) return false;
        return new Date() > new Date(this.deadline);
    }
}

// Simulates a database layer
class TaskRepository {
    constructor() {
        this.storage = [];
    }

    async save(task) {
        // Simulate async delay
        return new Promise((resolve) => {
            setTimeout(() => {
                this.storage.push(task);
                resolve(true);
            }, 100);
        });
    }

    getAll() {
        return this.storage;
    }
}

// Manages task creation and validation
class TaskManager {
    constructor(repository) {
        this.repository = repository;
    }

    validateName(name) {
        return typeof name === 'string' && name.trim().length > 0;
    }

    async addTask(name, priority = "normal", deadline = null) {
        if (!this.validateName(name)) {
            throw new Error("Task name is invalid.");
        }

        const task = new Task(name, priority, deadline);
        const success = await this.repository.save(task);

        if (!success) {
            throw new Error("Failed to save task.");
        }

        return task;
    }
}

// Usage
(async () => {
    const repo = new TaskRepository();
    const manager = new TaskManager(repo);

    await manager.addTask("Write tests", "high", "2025-05-01");
})();
