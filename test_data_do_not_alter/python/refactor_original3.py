def report_user_activity(user):
    print(f"{user.name} logged in at {user.login_time}")
    if user.failed_attempts > 3:
        print("User had multiple failed login attempts")
