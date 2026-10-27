def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """
    results = []

    for i in people:
        masked = {}
        if "name" in i:
            masked["name"] = i["name"]

        if "email" in i:
            local_part, domain = i["email"].split("@", 1)
            masked["email"] = ("*" * len(local_part)) + "@" + domain
            
        if "phone" in i:
            phone = i["phone"]
            masked["phone"] = "*" * (len(phone) - 2) + phone[-2:]

        results.append(masked)
    return results