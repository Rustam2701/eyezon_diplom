from selene import browser, have
import allure


class CatalogCartoonContent:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def open_catalog(self):
        with allure.step('Open catalog Cartoon'):
            browser.element('[data-test="menu_section_kids"]').click()

    def assert_text_cartoon(self):
        with allure.step('Catalog must have "Мультфильмы смотреть онлайн"'):
            browser.element('[class=headerBar__title]').should(have.text('Мультфильмы смотреть онлайн'))


catalog_content = CatalogCartoonContent()
