let tasks = [];

function saveToDatabase(task) {
    return new Promise((resolve) => {
        setTimeout(() => resolve(true), 100);
    });
}

function isValidTaskName(name) {
    return typeof name === 'string' && name.trim().length > 0;
}

async function addTask(name, priority = "normal") {
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

    const success = await saveToDatabase(task);

    if (!success) {
        throw new Error("Failed to save task.");
    }

    return task;
}
