import java.time.Duration;
import java.time.LocalDateTime;

public class UserActivity {

    public static void logLoginTime(User user) {
        System.out.println(user.getName() + " logged in at " + user.getLoginTime());
    }

    public static void logSessionDuration(User user) {
        Duration sessionLength = Duration.between(user.getLoginTime(), user.getLogoutTime());
        System.out.println("Session duration: " + sessionLength.getSeconds() + " seconds");
    }

    public static void warnFailedAttempts(User user) {
        if (user.getFailedAttempts() > 3) {
            System.out.println("User had multiple failed login attempts");
        }
    }

    public static void warnPasswordExpiry(User user) {
        Duration passwordAge = Duration.between(user.getPasswordLastChanged(), user.getLoginTime());
        if (passwordAge.toDays() > 90) {
            System.out.println("User password may be expired");
        }
    }

    public static void reportUserActivity(User user) {
        logLoginTime(user);
        logSessionDuration(user);
        warnFailedAttempts(user);
        warnPasswordExpiry(user);
    }
}
