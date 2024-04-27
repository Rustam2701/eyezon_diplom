from selene import browser, have
import allure


class AuthButton:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def click_auth_button(self):
        with allure.step('Auth button clickable'):
            browser.element('[data-test=header_avatar]').click()

    def auth_pages_have_text_about_qr(self):
        with allure.step('Auth page has text about QR'):
            browser.element('.qrBlock__title').should(have.text('Наведи камеру телефона на QR'))


auth_button = AuthButton()
