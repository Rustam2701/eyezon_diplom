from selene import browser, be, have
import allure


class FooterDemo:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def click_demo_button(self):
        with allure.step('Checking right transition to section'):
            browser.element('[class="block_eyezon_360__btn-link"]').click()

    def assert_demo_section_in_footer(self):
        with allure.step('User see footer section of DEMO data'):
            browser.element('#wf-form-request-a-demo').should(have.text('запросить демо.'))


demo_footer = FooterDemo()
