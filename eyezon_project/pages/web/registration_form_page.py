from selene import browser, have
import allure


class RequiredFieldsRegistration:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def auth_button_click(self):
        with allure.step('Auth button click'):
            browser.element('.header__btn-login').click()

    def registration_button_click(self):
        with allure.step('Registration button click'):
            with allure.step('Assert "Возможно, тебя заинтересует"'):
                browser.element('[type="button"]').click()

    def click_button_next(self):
        with allure.step('Click "Next" in registration window without filled required fields'):
            browser.element('[type="submit"]').click()

    def assert_notifications_about_required_fields(self):
        with allure.step('Assert text that fields are required'):
            browser.element('[class="ant-form-item-explain-error"]').should(have.text('Required field'))


required_fields_registration = RequiredFieldsRegistration()
