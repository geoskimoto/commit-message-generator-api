import java.util.Map;

public class RoleChecker {
    private static final Map<String, String> roleMap = Map.of(
        "admin", "Administrator",
        "user", "User"
    );

    public static String getRole(String role) {
        return roleMap.getOrDefault(role, "Unknown");
    }
}
