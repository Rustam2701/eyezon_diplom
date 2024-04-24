from selene import browser
import allure


class AuthButton:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def click_auth_button(self):
        with allure.step('Films button clickable'):
            browser.element('[data-test=header_avatar]').click()


auth_button = AuthButton()
