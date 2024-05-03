import allure
from eyezon_project.pages.web.authorization_invalid_email_page import auth_invalid_email


@allure.title("Authorization button clickable")
def test_clickable_auth_button():
    auth_invalid_email.open()

    auth_invalid_email.click_auth_button()

    auth_invalid_email.type_invalid_email()

    auth_invalid_email.notification_invalid_email()
