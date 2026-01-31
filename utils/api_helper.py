import requests

BASE_URL = "https://demoqa.com"

def login_api(username, password):
    response = requests.post(
        f"{BASE_URL}/Account/v1/GenerateToken",
        json={
            "userName": username,
            "password": password
        }
    )
