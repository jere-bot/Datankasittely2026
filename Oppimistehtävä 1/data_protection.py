def anonymize_and_mask(users):
    result = []

    for i in users:
        masked = i.copy()
        if "name" in i:
            masked["name"] = anonymize(i["name"])
        if "phone" in i:
            masked["phone"] = mask(i["phone"])
        result.append(masked)
        
    return result

def anonymize(name):
    anonymized = name[:1]
    return anonymized


def mask(phone):
    masked = "*" * (len(phone) - 2) + phone[-2:]
    return masked