from selene import browser, have
import allure


class CatalogCartoonContent:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def click_auth_button(self):
        with allure.step('Auth button clickable'):
            browser.element('.header__btn-login').click()

    def open_catalog(self):
        with allure.step('Open catalog Cartoon'):
            browser.element('[id="login_password"]').type('423423gdfdvdf')

    def assert_text_cartoon(self):
        with allure.step('Catalog must have "Мультфильмы смотреть онлайн"'):
            browser.element('[data-icon="eye-invisible"]').click()

    def assert_text_password(self):
        browser.element('#login_password').should(have.value('423423gdfdvdf'))


catalog_content = CatalogCartoonContent()
