import allure
from eyezon_project.pages.web.authorization_page import auth_invalid_email, auth_empty_password


@allure.title("Authorization not possible with invalid email")
def test_auth_with_invalid_email():
    auth_invalid_email.open()

    auth_invalid_email.click_auth_button()

    auth_invalid_email.type_invalid_email()

    auth_invalid_email.notification_invalid_email()


@allure.title('Auth not possible with empty password field')
def test_auth_empty_password():
    auth_empty_password.open()

    auth_empty_password.auth_button_click()

    auth_empty_password.type_user_data_with_empty_password()

    auth_empty_password.assert_required_field()
