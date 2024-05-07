from selene import browser, have
import allure


class HowItWorks:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def click_button_how_it_works(self):
        with allure.step('Clickable button "How it works"'):
            browser.element('[class="header__menu-link"]').click()

    def assert_title_section_how_it_works(self):
        with allure.step('User can see right title and video'):
            browser.element('[class="how-works__title"]').should(have.text('Как это работает'))


how_it_works = HowItWorks()
