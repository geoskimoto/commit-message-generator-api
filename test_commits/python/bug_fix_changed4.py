class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class UserManagerOriginal:
    def __init__(self):
        self.users = []

    def add_user(self, first_name, last_name):
        self.users.append(User(first_name, last_name))

    def get_user_full_name(self, index):
        user = self.users[index]
        return f"{user.first_name} {user.last_name}"

if __name__ == "__main__":
    manager = UserManagerOriginal()
    manager.add_user("Alice", "Johnson")
    manager.add_user("Bob", None)

    print(manager.get_user_full_name(0))
    print(manager.get_user_full_name(1))
