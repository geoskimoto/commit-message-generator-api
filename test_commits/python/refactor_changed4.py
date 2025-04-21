def log_login_time(user):
    print(f"{user.name} logged in at {user.login_time}")

def log_session_duration(user):
    session_length = (user.logout_time - user.login_time).seconds
    print(f"Session duration: {session_length} seconds")

def warn_failed_attempts(user):
    if user.failed_attempts > 3:
        print("User had multiple failed login attempts")

def warn_password_expiry(user):
    if (user.login_time - user.password_last_changed).days > 90:
        print("User password may be expired")

def report_user_activity(user):
    log_login_time(user)
    log_session_duration(user)
    warn_failed_attempts(user)
    warn_password_expiry(user)
