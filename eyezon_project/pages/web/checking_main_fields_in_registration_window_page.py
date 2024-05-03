from selene import browser, have
import allure


class FreeSubscriptionTitle:
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

    def click_button_next(self):
        with allure.step('Assert text in free subscription'):
            browser.element('[type="submit"]').click()

    def assert_notifications_about_required_fields(self):
        with allure.step('Assert text in free subscription'):
            browser.element('[class="ant-form-item-explain-error"]').should(have.text('Required field'))


free_subscription_title = FreeSubscriptionTitle()
