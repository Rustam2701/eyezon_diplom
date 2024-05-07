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
        with allure.step('Invalid email type'):
            browser.element('#login_username').type('sdfgsdf@bfdlfkgdlfg')
            browser.element('#login_password').click()

    def notification_invalid_email(self):
        with allure.step('Notification about invalid email'):
            browser.element('#login_username_help'). \
                should(have.text(
                'Looks like you entered the invalid email. Please, verify the email format: example@email.com'))


class AuthEmptyPassword:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def auth_button_click(self):
        with allure.step('Auth button clickable'):
            browser.element('.header__btn-login').click()

    def type_user_data_with_empty_password(self):
        with allure.step('User data'):
            browser.element('#login_username').type('test@test.com')
            browser.element('#login_password').click()
            browser.element('[id="login_country"]').type('Россия').press_enter()

    def assert_required_field(self):
        with allure.step('Assert not auth because password is required field'):
            browser.element('[class="ant-form-item-explain-error"]').should(have.text('Required field'))


auth_empty_password = AuthEmptyPassword()
auth_invalid_email = AuthInvalidEmail()
