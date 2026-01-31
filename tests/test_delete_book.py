import pytest
from pages.login_page import login_via_ui
from config import USERNAME, PASSWORD  # get credentials from local file

# Remove any CI-specific fixtures like setup_book if you are not using it
# Make sure you use the page fixture from playwright

@pytest.mark.parametrize("book_title", ["Some Book Title"])
def test_delete_book(page, book_title):
    login_via_ui(page, USERNAME, PASSWORD)
    # Your test steps here
