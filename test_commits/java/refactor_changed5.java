import java.time.Instant;
import java.util.Map;

public class AuthService {

    public static boolean isPasswordValid(User user, String password) {
        return user.getPassword().equals(password);
    }

    public static void incrementLoginAttempts(User user, Map<String, Integer> loginAttempts) {
        loginAttempts.put(user.getUsername(), loginAttempts.getOrDefault(user.getUsername(), 0) + 1);
        if (loginAttempts.get(user.getUsername()) > 5) {
            System.out.println("Account locked due to too many failed attempts");
        } else {
            System.out.println("Incorrect password");
        }
    }

    public static void resetLoginAttempts(User user, Map<String, Integer> loginAttempts) {
        loginAttempts.put(user.getUsername(), 0);
    }

    public static void logSuccessfulLogin(User user) {
        long now = Instant.now().toEpochMilli();
        user.setLastLogin(now);
        System.out.println(user.getUsername() + " logged in at " + now);
    }

    public static String generateToken(User user, String secret) {
        String payload = "{\"user_id\":\"" + user.getId() + "\",\"username\":\"" + user.getUsername() + "\",\"iat\":" + Instant.now().getEpochSecond() + "}";
        return JwtUtils.sign(payload, secret);
    }

    public static String handleLogin(User user, String password, Map<String, Integer> loginAttempts, String secret) {
        if (!isPasswordValid(user, password)) {
            incrementLoginAttempts(user, loginAttempts);
            return null;
        }

        resetLoginAttempts(user, loginAttempts);
        logSuccessfulLogin(user);
        return generateToken(user, secret);
    }
}
