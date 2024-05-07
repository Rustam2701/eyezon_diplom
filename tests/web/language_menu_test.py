import allure
from eyezon_project.pages.web.language_menu_page import language_menu


@allure.title("User can see menu language")
def test_visible_menu_checking_language():
    language_menu.open()

    language_menu.click_checking_language()

    language_menu.assert_visible_menu_checking_language()
