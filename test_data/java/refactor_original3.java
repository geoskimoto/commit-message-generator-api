public class AuthService {
    public boolean authenticate(String username, String password) {
        if (username.equals("admin") && password.equals("1234")) {
            return true;
        }
        return false;
    }
}
