from selene import browser, have
import allure


class FreeSubscriptionTitle:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def open_catalog_films(self):
        with allure.step('Open catalog films'):
            browser.element('[data-test="menu_section_films"]').click()

    def open_page_with_free_subscription(self):
        with allure.step('Open page with free subscription'):
            browser.element('[data-test="header_subscription_button"]').click()

    def assert_text_in_free_subscription(self):
        with allure.step('Assert text in free subscription'):
            browser.element('[class="segmentedLanding__title segmentedLanding__title_default"]') \
                .should(have.text('Подписка Иви'))


free_subscription_title = FreeSubscriptionTitle()
