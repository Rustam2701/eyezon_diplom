import allure
from eyezon_project.pages.web.visible_password_icon_eye_page import eye_icon_password_visible


@allure.title('User can see typed password by click on eye icon')
def test_catalog_has_cartoons():
    eye_icon_password_visible.open()

    eye_icon_password_visible.click_auth_button()

    eye_icon_password_visible.type_password()

    eye_icon_password_visible.click_eye_icon_visible_password()

    eye_icon_password_visible.password_should_be_visible()
