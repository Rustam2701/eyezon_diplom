from selene import browser, be
import allure

class VisibleMenuCheckLanguage:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def click_checking_language(self):
        browser.element('#w-dropdown-toggle-0').click()

    def assert_visible_menu_checking_language(self):
        browser.element('#w-dropdown-list-0').should(be.visible)


visible_menu_check_language = VisibleMenuCheckLanguage()