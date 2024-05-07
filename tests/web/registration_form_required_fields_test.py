import allure
from eyezon_project.pages.web.registration_form_required_fields_page import registration_form


@allure.title('Valid data first page registration')
def test_first_window_valid_data():
    registration_form.open()

    registration_form.auth_button_click()

    registration_form.registration_button_click()

    registration_form.type_first_name()

    registration_form.type_last_name()

    registration_form.check_country()

    registration_form.click_submit_button()

    registration_form.assert_second_window_registration()
