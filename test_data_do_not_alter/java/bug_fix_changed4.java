import java.util.ArrayList;
import java.util.List;

public class UserManagerFixed {
    private List<User> users;

    public UserManagerFixed() {
        this.users = new ArrayList<>();
    }

    public void addUser(String firstName, String lastName) {
        users.add(new User(firstName, lastName));
    }

    public String getUserFullName(int index) {
        User user = users.get(index);

        if ((user.firstName == null || user.firstName.isEmpty()) &&
            (user.lastName == null || user.lastName.isEmpty())) {
            throw new IllegalArgumentException("User name information is missing");
        }

        if (user.firstName == null || user.firstName.isEmpty()) {
            return user.lastName;
        }

        if (user.lastName == null || user.lastName.isEmpty()) {
            return user.firstName;
        }

        return user.firstName + " " + user.lastName;
    }

    public static void main(String[] args) {
        UserManagerFixed manager = new UserManagerFixed();
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
