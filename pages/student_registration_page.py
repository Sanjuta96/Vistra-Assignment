from playwright.sync_api import Page

class StudentRegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://demoqa.com/automation-practice-form"

    def open(self):
        self.page.goto(self.url, timeout=60000)

    def fill_first_name(self, first_name):
        self.page.locator("#firstName").fill(first_name)

    def fill_last_name(self, last_name):
        self.page.locator("#lastName").fill(last_name)

    def fill_email(self, email):
        self.page.locator("#userEmail").fill(email)

    def select_gender(self, gender):
        gender_map = {"Male": "1", "Female": "2", "Other": "3"}
        self.page.locator(f"label[for='gender-radio-{gender_map[gender]}']").click()

    def fill_mobile(self, mobile):
        self.page.locator("#userNumber").fill(mobile)

    def fill_dob(self, dob):
        self.page.locator("#dateOfBirthInput").click()
        self.page.locator(".react-datepicker__month-select").select_option(dob["month"])
        self.page.locator(".react-datepicker__year-select").select_option(str(dob["year"]))
        self.page.locator(f".react-datepicker__day--0{dob['day']:02d}").click()

    def select_subjects(self, subjects):
        input_locator = self.page.locator("#subjectsInput")
        for subject in subjects:
            input_locator.fill(subject)
            option_locator = self.page.locator(
                f".subjects-auto-complete__option:has-text('{subject}')"
            )
            option_locator.wait_for(state="visible")
            option_locator.first.click()

    def select_hobbies(self, hobbies):
        hobby_map = {"Sports":1, "Reading":2, "Music":3}
        for hobby in hobbies:
            self.page.locator(f"label[for='hobbies-checkbox-{hobby_map[hobby]}']").click()

    def upload_picture(self, file_path: str):
        upload = self.page.locator("#uploadPicture")
        upload.scroll_into_view_if_needed()
        upload.set_input_files(file_path)

    def fill_address(self, address):
        self.page.locator("#currentAddress").fill(address)

    def select_state(self, state):
        self.page.locator("#state").click()
        self.page.locator(f"div[id^='react-select-3-option']:has-text('{state}')").click()

    def select_city(self, city):
        self.page.locator("#city").click()
        self.page.locator(f"div[id^='react-select-4-option']:has-text('{city}')").click()

    def submit_form(self):
        self.page.locator("#submit").click()

    def get_modal_data(self):
        modal = self.page.locator(".modal-content")
        modal.wait_for(state="visible")
        header = modal.locator("#example-modal-sizes-title-lg").inner_text()
        rows = modal.locator("table tbody tr")
        data = {}
        for i in range(rows.count()):
            cells = rows.nth(i).locator("td")
            key = cells.nth(0).inner_text().strip()
            value = cells.nth(1).inner_text().strip()
            data[key] = value
        return header, data

    def close_modal(self):
        self.page.locator("#closeLargeModal").click()
