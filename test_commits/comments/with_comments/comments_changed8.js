let tasks = [];

// Simulate a database save with a timeout
function saveToDatabase(task) {
    return new Promise((resolve) => {
        setTimeout(() => resolve(true), 100);
    });
}

// Validates a task name
function isValidTaskName(name) {
    return typeof name === 'string' && name.trim().length > 0;
}

// Adds a task with validation and async "save"
async function addTask(name, priority = "normal") {
    // Validate task name
    if (!isValidTaskName(name)) {
        throw new Error("Invalid task name.");
    }

    const task = {
        name: name.trim(),
        completed: false,
        priority,
        createdAt: new Date().toISOString()
    };

    tasks.push(task);

    // Simulate saving to a database
    const success = await saveToDatabase(task);

    if (!success) {
        throw new Error("Failed to save task.");
    }

    return task;
}
