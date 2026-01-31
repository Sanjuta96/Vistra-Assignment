from playwright.sync_api import Page, TimeoutError

class ProfilePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_book(self, book_name: str, timeout=20000):
        self.page.locator(".rt-tbody").wait_for(state="visible", timeout=timeout)

        row_locator = self.page.locator(
            f".rt-tr-group:has(.rt-td:has-text('{book_name}'))"
        )

        try:
            row_locator.first.wait_for(state="visible", timeout=timeout)
            return row_locator.first
        except TimeoutError:
            raise Exception(
                f"Book '{book_name}' not found in profile table after {timeout}ms"
            )

    def delete_book(self, book_name: str):
        row = self.wait_for_book(book_name)

        delete_button = row.locator("span[title='Delete']")
        delete_button.wait_for(state="visible", timeout=5000)
        delete_button.scroll_into_view_if_needed()
        delete_button.click(force=True)

        confirm_btn = self.page.locator("#closeSmallModal-ok")
        confirm_btn.wait_for(state="visible", timeout=5000)
        confirm_btn.click()

        row.wait_for(state="detached", timeout=10000)
