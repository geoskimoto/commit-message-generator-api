import time
import jwt

def handle_login(user, password, login_attempts, secret):
    if user.password != password:
        login_attempts[user.username] = login_attempts.get(user.username, 0) + 1
        if login_attempts[user.username] > 5:
            print("Account locked due to too many failed attempts")
        else:
            print("Incorrect password")
        return None

    login_attempts[user.username] = 0
    user.last_login = time.time()
    print(f"{user.username} logged in at {user.last_login}")
    
    payload = {
        "user_id": user.id,
        "username": user.username,
        "iat": int(time.time())
    }
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token
