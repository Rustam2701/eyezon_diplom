import allure
from eyezon_project.pages.web.authorization_empty_password_page import notifications_title


@allure.title('Check notifications text')
def test_notifications_text():
    notifications_title.open()

    notifications_title.auth_button_click()

    notifications_title.type_invalid_password()

    notifications_title.assert_not_auth()
