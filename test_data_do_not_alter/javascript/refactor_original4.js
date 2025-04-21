function reportUserActivity(user) {
    console.log(`${user.name} logged in at ${user.loginTime}`);
    const sessionLength = (user.logoutTime - user.loginTime) / 1000;
    console.log(`Session duration: ${sessionLength} seconds`);
    if (user.failedAttempts > 3) {
        console.log("User had multiple failed login attempts");
    }
    const passwordAge = (user.loginTime - user.passwordLastChanged) / (1000 * 60 * 60 * 24);
    if (passwordAge > 90) {
        console.log("User password may be expired");
    }
}
