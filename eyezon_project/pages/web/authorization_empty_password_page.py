from selene import browser, have
import allure


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
