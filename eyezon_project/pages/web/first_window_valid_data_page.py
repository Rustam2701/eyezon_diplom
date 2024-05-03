from selene import browser, have, be
import allure


class FirstPageValidData:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def auth_button_click11(self):
        with allure.step('Auth button clickable'):
            browser.element('.header__btn-login').click()

    def registration_button_click22(self):
        with allure.step('Recommendation title'):
            with allure.step('Assert "Возможно, тебя заинтересует"'):
                browser.element('[type="button"]').click()

    def type_first_name(self):
        with allure.step('Assert text in free subscription'):
            browser.element('#personalData_firstName').type('Иван')

    def type_last_name(self):
        with allure.step('Assert text in free subscription'):
            browser.element('#personalData_lastName').type('Иванов')

    def check_country(self):
        with allure.step('Assert text in free subscription'):
            browser.element('#personalData_businessCountry').type('Россия').press_enter()

    def click_submit_button(self):
        with allure.step('Assert text in free subscription'):
            browser.element('[type="submit"]').click()

    def assert_second_window_registration(self):
        with allure.step('Assert text in free subscription'):
            browser.element('[class="ant-steps-item-description"]').should(be.visible)


first_page_valid_data = FirstPageValidData()
