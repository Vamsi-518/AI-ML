import requests
API_URL = "https://jsonplaceholder.typicode.com/users"
def get_students():
    try:
        response = requests.get(
            API_URL,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print("API Error:", error)
        return []
def get_student(student_id):
    try:
        url = f"{API_URL}/{student_id}"
        response = requests.get(
            url,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print("API Error:", error)
        return None