import java.time.LocalDateTime;

public class Notification {
    private String message;
    private LocalDateTime timestamp;
    private boolean read;

    public Notification(String message) {
        this.message = message;
        this.timestamp = LocalDateTime.now();
        this.read = false;
    }

    public void markAsRead() {
        this.read = true;
    }
}
