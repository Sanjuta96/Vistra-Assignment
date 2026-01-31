# conftest.py
import os
import pytest
from playwright.sync_api import sync_playwright

# Get credentials from config.py or environment variables
try:
    from config import USERNAME, PASSWORD
except ImportError:
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

def get_credentials():
    if not USERNAME or not PASSWORD:
        raise RuntimeError("USERNAME and PASSWORD must be provided")
    return USERNAME, PASSWORD

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
