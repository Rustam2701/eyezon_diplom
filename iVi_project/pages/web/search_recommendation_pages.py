from selene import browser, have
import allure


class SearchRecommendations:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def open_search_field(self):
        with allure.step('Open Search field'):
            browser.element('[data-test="header_search"]').click()

    def assert_recommendation_title(self):
        with allure.step('Recommendation title'):
            with allure.step('Assert "Возможно, тебя заинтересует"'):
                browser.element('.searchBlock__title').should(have.text('Возможно, тебя заинтересует'))


search_recommendations = SearchRecommendations()
