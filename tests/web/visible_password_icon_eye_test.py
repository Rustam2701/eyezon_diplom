import allure
from eyezon_project.pages.web.visible_password_icon_eye_page import catalog_content

@allure.title('Catalog "Мультфильмы" contents')
def test_catalog_has_cartoons():
    catalog_content.open()

    catalog_content.click_auth_button()

    catalog_content.open_catalog()

    catalog_content.assert_text_cartoon()

    catalog_content.assert_text_password()