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

    public String getInitials() {
        return firstName.charAt(0) + "." + lastName.charAt(0) + ".";
    }
}
