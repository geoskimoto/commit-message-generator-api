public class User {
    private String firstName;
    private String lastName;

    public User(String first, String last) {
        this.firstName = first;
        this.lastName = last;
    }

    public String getFullName() {
        return firstName + " " + lastName;
    }
}
