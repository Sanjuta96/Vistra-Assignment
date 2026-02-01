import pytest
from pages.login_page import login_via_ui
from config import USERNAME, PASSWORD  # get credentials from local file

@pytest.mark.parametrize("book_title", ["Some Book Title"])
def test_delete_book(page, book_title):
    login_via_ui(page, USERNAME, PASSWORD)
