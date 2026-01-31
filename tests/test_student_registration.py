import os
import pytest
from pages.student_registration_page import StudentRegistrationPage

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "Assets")

@pytest.mark.parametrize("student_data", [
    {
        "first_name": "Sanju",
        "last_name": "Tidke",
        "email": "xyz@gmail.com",
        "gender": "Female",
        "mobile": "9876543210",
        "dob": {"day": 23, "month": "May", "year": 1996},
        "subjects": ["English"],
        "picture": os.path.join(ASSETS_DIR, "test_image.webp"),
        "hobbies": ["Music"],
        "address": "123 Main Street, City",
        "state": "NCR",
        "city": "Delhi"
    }
])
def test_register_student_form(page, student_data):
    assert os.path.exists(student_data["picture"]), "Test image not found"

    registration = StudentRegistrationPage(page)
    registration.open()

    # Fill the form
    registration.fill_first_name(student_data["first_name"])
    registration.fill_last_name(student_data["last_name"])
    registration.fill_email(student_data["email"])
    registration.select_gender(student_data["gender"])
    registration.fill_mobile(student_data["mobile"])
    registration.fill_dob(student_data["dob"])
    registration.select_subjects(student_data["subjects"])
    registration.select_hobbies(student_data["hobbies"])
    registration.upload_picture(student_data["picture"])
    registration.fill_address(student_data["address"])
    registration.select_state(student_data["state"])
    registration.select_city(student_data["city"])
    registration.submit_form()

    # Get modal data
    header, modal_data = registration.get_modal_data()

    # Check header
    assert header == "Thanks for submitting the form"

    # Validate each field
    expected_data = {
        "Student Name": f"{student_data['first_name']} {student_data['last_name']}",
        "Student Email": student_data["email"],
        "Gender": student_data["gender"],
        "Mobile": student_data["mobile"],
        "Date of Birth": f"{student_data['dob']['day']:02d} {student_data['dob']['month']},{student_data['dob']['year']}",
        "Subjects": ", ".join(student_data["subjects"]),
        "Hobbies": ", ".join(student_data["hobbies"]),
        "Picture": os.path.basename(student_data["picture"]),
        "Address": student_data["address"],
        "State and City": f"{student_data['state']} {student_data['city']}"
    }

    for key, expected_value in expected_data.items():
        actual_value = modal_data.get(key)
        assert actual_value == expected_value, f"Mismatch in {key}: expected '{expected_value}', got '{actual_value}'"

    # Close the modal
def close_modal(self):
    self.page.evaluate("document.querySelector('#fixedban').style.display='none'")
    self.page.locator("#closeLargeModal").click()


