def validate_login_data(data):

    required_fields = [
        "email",
        "password"
    ]

    for field in required_fields:
        if not data.get(field):
            return False, f"{field} is required"

    return True, "Login data is valid"