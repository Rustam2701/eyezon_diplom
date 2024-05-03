import time

from selene import browser, have
import allure


class NotificationsTitle:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def auth_button_click(self):
        with allure.step('Auth button clickable'):
            browser.element('.header__btn-login').click()

    def type_invalid_password(self):
        with allure.step('Invalid email'):
            browser.element('#login_username').type('test@test.com')
            browser.element('#login_password').click()
            browser.element('[id="login_country"]').type('Россия').press_enter()

    def assert_not_auth(self):
        browser.element('[class="ant-form-item-explain-error"]'). \
            should(have.text('Required field'))


notifications_title = NotificationsTitle()
