import java.util.ArrayList;
import java.util.List;

class Task {
    private String name;
    private boolean completed;

    public Task(String name) {
        this.name = name;
        this.completed = false;
    }

    public String getName() {
        return name;
    }

    public boolean isCompleted() {
        return completed;
    }
}

class TaskManager {
    private List<Task> tasks = new ArrayList<>();

    public void addTask(String name) {
        tasks.add(new Task(name));
    }

    public List<Task> getAllTasks() {
        return tasks;
    }
}
