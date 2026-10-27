from datetime import datetime

def anonymize(people):
    """
    TODO: Anonymize data:
    - remove name
    - keep only birth year
    - keep only first letter of city
    - return same datastructure with anonymized data
    """
    result = []

    for i in people:
        if "birthdate" in i:
            birthDate = int(i["birthdate"][:4])

        if "city" in i:
            city = i["city"][:1]
        result.append({"birth_year": birthDate, "city_initial": city})
        
    return result