import java.util.ArrayList;
import java.util.Date;
import java.util.List;

class Task {
    private String name;
    private boolean completed;
    private Date createdAt;
    private Date completedAt;
    private String priority;

    public Task(String name, String priority) {
        this.name = name;
        this.completed = false;
        this.createdAt = new Date();
        this.priority = priority;
        this.completedAt = null;
    }

    public void markComplete() {
        this.completed = true;
        this.completedAt = new Date();
    }

    public String getName() {
        return name;
    }

    public boolean isCompleted() {
        return completed;
    }

    public String getPriority() {
        return priority;
    }
}

class TaskManager {
    private List<Task> tasks = new ArrayList<>();

    public void addTask(String name, String priority) {
        tasks.add(new Task(name, priority));
    }

    public List<Task> getAllTasks() {
        return tasks;
    }

    public List<Task> getCompletedTasks() {
        List<Task> result = new ArrayList<>();
        for (Task task : tasks) {
            if (task.isCompleted()) {
                result.add(task);
            }
        }
        return result;
    }

    public List<Task> getTasksByPriority(String priority) {
        List<Task> result = new ArrayList<>();
        for (Task task : tasks) {
            if (task.getPriority().equals(priority)) {
                result.add(task);
            }
        }
        return result;
    }
}
