class UserManager {
    constructor() {
        this.users = [];
    }

    addUser(firstName, lastName) {
        this.users.push({ firstName, lastName });
    }

    getUserFullName(index) {
        const user = this.users[index];

        if (!user.firstName && !user.lastName) {
            throw new Error("User name information is missing");
        }

        if (!user.firstName) return user.lastName;
        if (!user.lastName) return user.firstName;

        return `${user.firstName} ${user.lastName}`;
    }
}

const manager = new UserManager();
manager.addUser("Alice", "Johnson");
manager.addUser("Bob", null); 

console.log(manager.getUserFullName(0)); 
console.log(manager.getUserFullName(1)); 