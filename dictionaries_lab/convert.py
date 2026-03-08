def convert(data):
    result = {}
    for item in data:
        category = item["type"]
        if category not in result:
            result[category] = {}
        result[category][item["name"]] = item["price"]
    return result