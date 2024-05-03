import allure
from eyezon_project.pages.web.visible_menu_check_language_page import visible_menu_check_language


def test_visible_menu_checking_language():
    visible_menu_check_language.open()

    visible_menu_check_language.click_checking_language()

    visible_menu_check_language.assert_visible_menu_checking_language()
