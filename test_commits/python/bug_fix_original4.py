class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class UserManagerFixed:
    def __init__(self):
        self.users = []

    def add_user(self, first_name, last_name):
        self.users.append(User(first_name, last_name))

    def get_user_full_name(self, index):
        user = self.users[index]

        if not user.first_name and not user.last_name:
            raise ValueError("User name information is missing")

        if not user.first_name:
            return user.last_name

        if not user.last_name:
            return user.first_name

        return f"{user.first_name} {user.last_name}"

if __name__ == "__main__":
    manager = UserManagerFixed()
    manager.add_user("Alice", "Johnson")
    manager.add_user("Bob", None)

    print(manager.get_user_full_name(0))
    print(manager.get_user_full_name(1))
