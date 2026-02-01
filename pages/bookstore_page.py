class BookStorePage:
    def __init__(self, page):
        self.page = page
        self.search_box = "#searchBox"

    def open(self):
        """ Navigate to Book Store page. """
        self.page.goto("https://demoqa.com/books")

    def search_book(self, book_name):
        self.page.locator("#searchBox").fill(book_name)
        self.page.wait_for_timeout(1500)  # wait for table to refresh

    def has_book(self, book_name):
        """ Returns True if book exists in search results. """
        book_locator = self.page.locator(f"a:has-text('{book_name}')")
        return book_locator.count() > 0 and book_locator.first.is_visible()
