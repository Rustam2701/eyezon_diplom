from selene import browser, have
import allure


class AuthInvalidEmail:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def click_auth_button(self):
        with allure.step('Auth button clickable'):
            browser.element('.header__btn-login').click()

    def type_invalid_email(self):
        with allure.step('Invalid email'):
            browser.element('#login_username').type('sdfgsdf@bfdlfkgdlfg')
            browser.element('#login_password').click()

    def notification_invalid_email(self):
        with allure.step('Notification about invalid email'):
            browser.element('#login_username_help'). \
                should(have.text(
                'Looks like you entered the invalid email. Please, verify the email format: example@email.com'))


auth_invalid_email = AuthInvalidEmail()
