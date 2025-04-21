import java.time.Duration;
import java.time.LocalDateTime;

public class UserActivity {

    public static void reportUserActivity(User user) {
        System.out.println(user.getName() + " logged in at " + user.getLoginTime());

        Duration sessionLength = Duration.between(user.getLoginTime(), user.getLogoutTime());
        System.out.println("Session duration: " + sessionLength.getSeconds() + " seconds");

        if (user.getFailedAttempts() > 3) {
            System.out.println("User had multiple failed login attempts");
        }

        Duration passwordAge = Duration.between(user.getPasswordLastChanged(), user.getLoginTime());
        if (passwordAge.toDays() > 90) {
            System.out.println("User password may be expired");
        }
    }
}
