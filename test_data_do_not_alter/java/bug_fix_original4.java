import java.util.ArrayList;
import java.util.List;

public class UserManagerOriginal {
    private List<User> users;

    public UserManagerOriginal() {
        this.users = new ArrayList<>();
    }

    public void addUser(String firstName, String lastName) {
        users.add(new User(firstName, lastName));
    }

    public String getUserFullName(int index) {
        User user = users.get(index);
        return user.firstName + " " + user.lastName;
    }

    public static void main(String[] args) {
        UserManagerOriginal manager = new UserManagerOriginal();
        manager.addUser("Alice", "Johnson");
        manager.addUser("Bob", null);

        System.out.println(manager.getUserFullName(0));
        System.out.println(manager.getUserFullName(1));
    }

    private static class User {
        String firstName;
        String lastName;

        User(String firstName, String lastName) {
            this.firstName = firstName;
            this.lastName = lastName;
        }
    }
}
