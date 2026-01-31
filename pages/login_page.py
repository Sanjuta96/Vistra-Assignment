
from config import USERNAME, PASSWORD

def login_via_ui(page, username, password):
    page.goto("https://demoqa.com/login", timeout=60000)
    page.fill("#userName", username)
    page.fill("#password", password)
    page.click("#login")

    # Wait for Profile page to load
    # page.wait_for_url("https://demoqa.com/profile", timeout=10000)
