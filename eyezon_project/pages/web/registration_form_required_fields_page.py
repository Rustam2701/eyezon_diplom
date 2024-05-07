from selene import browser, be
import allure


class FirstPageValidData:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def auth_button_click(self):
        with allure.step('Auth button click'):
            browser.element('.header__btn-login').click()

    def registration_button_click(self):
        with allure.step('Registration button click'):
            browser.element('[type="button"]').click()

    def type_first_name(self):
        with allure.step('Type First name'):
            browser.element('#personalData_firstName').type('Иван')

    def type_last_name(self):
        with allure.step('Type Last name'):
            browser.element('#personalData_lastName').type('Иванов')

    def check_country(self):
        with allure.step('Check country'):
            browser.element('#personalData_businessCountry').type('Россия').press_enter()

    def click_submit_button(self):
        with allure.step('Click button "Next"'):
            browser.element('[type="submit"]').click()

    def assert_second_window_registration(self):
        with allure.step('Next page of registration should be visible'):
            browser.element('[class="ant-steps-item-description"]').should(be.visible)


registration_form = FirstPageValidData()
