import allure
from eyezon_project.pages.web.authrorization_form_page import auth_form


@allure.title('User can see typed password by click on eye icon')
def test_catalog_has_cartoons():
    auth_form.open()

    auth_form.click_auth_button()

    auth_form.type_password()

    auth_form.click_eye_icon_visible_password()

    auth_form.password_should_be_visible()
