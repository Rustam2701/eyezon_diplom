import allure
from eyezon_project.pages.web.checking_main_fields_in_registration_window_page import required_fields_registration


@allure.title('User don`t register without filling required fields')
def test_register_with_empty_required_fields():
    required_fields_registration.open()

    required_fields_registration.auth_button_click()

    required_fields_registration.registration_button_click()

    required_fields_registration.click_button_next()

    required_fields_registration.assert_notifications_about_required_fields()
