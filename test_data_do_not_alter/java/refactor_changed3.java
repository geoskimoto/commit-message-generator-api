public class AuthService {
    private boolean isAdmin(String username, String password) {
        return username.equals("admin") && password.equals("1234");
    }

    public boolean authenticate(String username, String password) {
        return isAdmin(username, password);
    }
}
