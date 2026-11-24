def validate_company_data(data):

    required_fields = [
        "company_name",
        "full_name",
        "email",
        "password"
    ]

    for field in required_fields:
        if not data.get(field):
            return False, f"{field} is required"

    if len(data["password"]) < 8:
        return False, "Password must be at least 8 characters"

    if "@" not in data["email"]:
        return False, "Invalid email address"

    return True, "Company data is valid"