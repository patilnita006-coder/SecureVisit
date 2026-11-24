def validate_visitor_data(data):

    required_fields = [
        "full_name",
        "mobile",
        "visit_purpose",
        "device_type"
    ]

    for field in required_fields:
        if not data.get(field):
            return False, f"{field} is required"

    if len(data["mobile"]) < 10:
        return False, "Invalid mobile number"

    if data["device_type"].lower() not in ["android", "ios"]:
        return False, "Device type must be android or ios"

    return True, "Visitor data is valid"