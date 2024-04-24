from selene import browser, have
import allure


@allure.title('Visible button of free watching subscription in start page')
def test_visible_free_watching_button():
    with allure.step('Open catalog films'):
        browser.open('/')
        browser.element('[data-test="menu_section_films"]').click()

    with allure.step('Open page with free subscription'):
        browser.element('[data-test="header_subscription_button"]').click()

    with allure.step('Assert text in free subscription'):
        browser.element('[class="segmentedLanding__title segmentedLanding__title_default"]') \
            .should(have.text('Подписка Иви'))
