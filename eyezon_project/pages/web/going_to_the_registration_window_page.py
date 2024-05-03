from selene import browser, have
import allure


class SearchRecommendations:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def auth_button_click(self):
        with allure.step('Auth button clickable'):
            browser.element('.header__btn-login').click()

    def registration_button_click(self):
        with allure.step('Recommendation title'):
            with allure.step('Assert "Возможно, тебя заинтересует"'):
                browser.element('[type="button"]').click()

    def assert_registration_window(self):
        browser.element('[class="sc-fEXmlR fleiSJ"]').should(have.text('Sign Up'))


search_recommendations = SearchRecommendations()
