def report_user_activity(user):
    print(f"{user.name} logged in at {user.login_time}")
    session_length = (user.logout_time - user.login_time).seconds
    print(f"Session duration: {session_length} seconds")
    if user.failed_attempts > 3:
        print("User had multiple failed login attempts")
    if (user.password_last_changed - user.login_time).days > 90:
        print("User password may be expired")
