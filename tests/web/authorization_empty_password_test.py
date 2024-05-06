import allure
from eyezon_project.pages.web.authorization_empty_password_page import auth_empty_password


@allure.title('Auth not possible with empty password field')
def test_auth_empty_password():
    auth_empty_password.open()

    auth_empty_password.auth_button_click()

    auth_empty_password.type_user_data_with_empty_password()

    auth_empty_password.assert_required_field()
