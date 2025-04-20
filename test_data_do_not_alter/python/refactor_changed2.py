def get_role(role):
    return {
        'admin': 'Administrator',
        'user': 'User'
    }.get(role, 'Unknown')
