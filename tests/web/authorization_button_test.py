import allure
from iVi_project.pages.web.authorization_button import auth_button


@allure.title("Authorization button clickable")
def test_clickable_auth_button():
    auth_button.open()

    auth_button.click_auth_button()
