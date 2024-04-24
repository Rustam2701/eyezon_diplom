from selene import browser, have
import allure


@allure.title('Searching films')
def test_search_film():
    with allure.step('Open search field'):
        browser.open('/')
        browser.element('[data-test="header_search"]').click()

    with allure.step('Type text "Чебурашка"'):
        browser.element('[data-test="search_input"]').type('Чебурашка').press_enter()

    with allure.step('Assert film "Чебурашка"'):
        browser.element('.searchBlock.searchBlock_result').should(have.text('Чебурашка'))
