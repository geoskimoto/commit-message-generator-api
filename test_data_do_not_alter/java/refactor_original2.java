public class RoleChecker {
    public static String getRole(String role) {
        if (role.equals("admin")) {
            return "Administrator";
        } else if (role.equals("user")) {
            return "User";
        } else {
            return "Unknown";
        }
    }
}
