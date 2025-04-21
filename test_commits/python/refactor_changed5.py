import time
import jwt

def is_password_valid(user, password):
    return user.password == password

def increment_login_attempts(user, login_attempts):
    login_attempts[user.username] = login_attempts.get(user.username, 0) + 1
    if login_attempts[user.username] > 5:
        print("Account locked due to too many failed attempts")
    else:
        print("Incorrect password")

def reset_login_attempts(user, login_attempts):
    login_attempts[user.username] = 0

def log_successful_login(user):
    user.last_login = time.time()
    print(f"{user.username} logged in at {user.last_login}")

def generate_token(user, secret):
    payload = {
        "user_id": user.id,
        "username": user.username,
        "iat": int(time.time())
    }
    return jwt.encode(payload, secret, algorithm="HS256")

def handle_login(user, password, login_attempts, secret):
    if not is_password_valid(user, password):
        increment_login_attempts(user, login_attempts)
        return None

    reset_login_attempts(user, login_attempts)
    log_successful_login(user)
    return generate_token(user, secret)
