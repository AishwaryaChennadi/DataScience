import requests

def get_data(endpoint="/posts"):
    """Fetch data from JSONPlaceholder API"""
    url = f"https://jsonplaceholder.typicode.com{endpoint}"
    try:
        response = requests.get(url, timeout=5)
        return response   # return even if status != 200
    except requests.exceptions.RequestException:
        return None
