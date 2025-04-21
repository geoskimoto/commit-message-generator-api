const jwt = require("jsonwebtoken");

function isPasswordValid(user, password) {
    return user.password === password;
}

function incrementLoginAttempts(user, loginAttempts) {
    loginAttempts[user.username] = (loginAttempts[user.username] || 0) + 1;
    if (loginAttempts[user.username] > 5) {
        console.log("Account locked due to too many failed attempts");
    } else {
        console.log("Incorrect password");
    }
}

function resetLoginAttempts(user, loginAttempts) {
    loginAttempts[user.username] = 0;
}

function logSuccessfulLogin(user) {
    user.lastLogin = Date.now();
    console.log(`${user.username} logged in at ${user.lastLogin}`);
}

function generateToken(user, secret) {
    const payload = {
        userId: user.id,
        username: user.username,
        iat: Math.floor(Date.now() / 1000)
    };
    return jwt.sign(payload, secret);
}

function handleLogin(user, password, loginAttempts, secret) {
    if (!isPasswordValid(user, password)) {
        incrementLoginAttempts(user, loginAttempts);
        return null;
    }

    resetLoginAttempts(user, loginAttempts);
    logSuccessfulLogin(user);
    return generateToken(user, secret);
}
