from selene import browser, have
import allure


@allure.title('Catalog "Мультфильмы" contents')
def test_catalog_has_cartoons():
    with allure.step('Open catalog "Мультфильмы"'):
        browser.open('/')
        browser.element('[data-test="menu_section_kids"]').click()

    with allure.step('Catalog must have "Мультфильмы смотреть онлайн"'):
        browser.element('[class=headerBar__title]').should(have.text('Мультфильмы смотреть онлайн'))
