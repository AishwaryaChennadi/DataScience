def validate_status(response):
    if response and response.status_code == 200:
        return True, "Status code is 200"
    return False, f"Unexpected status code: {response.status_code if response else 'No Response'}"

def validate_schema(response):
    try:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            sample = data[0]
            required_keys = ["userId", "id", "title", "body"]
            for key in required_keys:
                if key not in sample:
                    return False, f"Missing key: {key}"
            if not isinstance(sample["id"], int):
                return False, "id is not int"
            if not isinstance(sample["title"], str):
                return False, "title is not str"
            return True, "Schema validated successfully"
        return False, "Response is not a valid list"
    except Exception as e:
        return False, f"Schema validation failed: {str(e)}"
