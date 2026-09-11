# ==========================================================
# MEDIINSIGHT AI
# AUTHENTICATION
# ==========================================================

USERS = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "name": "Administrator",
    },

    "doctor": {
        "password": "doctor123",
        "role": "doctor",
        "name": "Doctor",
    },

    "junior": {
        "password": "junior123",
        "role": "junior",
        "name": "Junior Doctor",
    },
}


def login(username: str, password: str):
    """
    Validate username and password.

    Returns:
        tuple:
            (True, user_data) if credentials are valid
            (False, None) otherwise
    """

    username = username.strip()

    if username not in USERS:
        return False, None

    user = USERS[username]

    if user["password"] != password:
        return False, None

    return True, user