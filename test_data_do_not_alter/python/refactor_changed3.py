def log_login(user):
    print(f"{user.name} logged in at {user.login_time}")

def check_failed_attempts(user):
    if user.failed_attempts > 3:
        print("User had multiple failed login attempts")

def report_user_activity(user):
    log_login(user)
    check_failed_attempts(user)
