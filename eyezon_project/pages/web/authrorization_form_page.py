from selene import browser, have
import allure


class EyeIconPasswordVisible:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def click_auth_button(self):
        with allure.step('Auth button clickable'):
            browser.element('.header__btn-login').click()

    def type_password(self):
        with allure.step('Typing password'):
            browser.element('#login_password').type('423423gdfdvdf')

    def click_eye_icon_visible_password(self):
        with allure.step('Click eye icon visible password'):
            browser.element('[data-icon="eye-invisible"]').click()

    def password_should_be_visible(self):
        with allure.step('User can see typed password'):
            browser.element('#login_password').should(have.value('423423gdfdvdf'))


auth_form = EyeIconPasswordVisible()
