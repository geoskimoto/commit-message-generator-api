from datetime import datetime

class Session:
    def __init__(self, user_id):
        self.user_id = user_id
        self.active = True
        self.created_at = datetime.utcnow()

    def end(self):
        self.active = False
        self.ended_at = datetime.utcnow()
