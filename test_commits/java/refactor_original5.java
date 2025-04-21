import java.time.Instant;
import java.util.Map;

public class AuthService {

    public static String handleLogin(User user, String password, Map<String, Integer> loginAttempts, String secret) {
        if (!user.getPassword().equals(password)) {
            loginAttempts.put(user.getUsername(), loginAttempts.getOrDefault(user.getUsername(), 0) + 1);
            if (loginAttempts.get(user.getUsername()) > 5) {
                System.out.println("Account locked due to too many failed attempts");
            } else {
                System.out.println("Incorrect password");
            }
            return null;
        }

        loginAttempts.put(user.getUsername(), 0);
        user.setLastLogin(Instant.now().toEpochMilli());
        System.out.println(user.getUsername() + " logged in at " + user.getLastLogin());

        String payload = "{\"user_id\":\"" + user.getId() + "\",\"username\":\"" + user.getUsername() + "\",\"iat\":" + Instant.now().getEpochSecond() + "}";
        return JwtUtils.sign(payload, secret);
    }
}
