from selene import browser, have
import allure


class RegistrationWay:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def auth_button_click(self):
        with allure.step('Auth button click'):
            browser.element('.header__btn-login').click()

    def registration_button_click(self):
        with allure.step('Registration button click'):
            browser.element('[type="button"]').click()

    def assert_registration_window(self):
        with allure.step('User must see registration window'):
            browser.element('[class="sc-fEXmlR fleiSJ"]').should(have.text('Sign Up'))


registration_way = RegistrationWay()
