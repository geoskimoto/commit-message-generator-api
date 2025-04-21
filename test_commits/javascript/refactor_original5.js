const jwt = require("jsonwebtoken");

function handleLogin(user, password, loginAttempts, secret) {
    if (user.password !== password) {
        loginAttempts[user.username] = (loginAttempts[user.username] || 0) + 1;
        if (loginAttempts[user.username] > 5) {
            console.log("Account locked due to too many failed attempts");
        } else {
            console.log("Incorrect password");
        }
        return null;
    }

    loginAttempts[user.username] = 0;
    user.lastLogin = Date.now();
    console.log(`${user.username} logged in at ${user.lastLogin}`);

    const payload = {
        userId: user.id,
        username: user.username,
        iat: Math.floor(Date.now() / 1000)
    };
    return jwt.sign(payload, secret);
}
