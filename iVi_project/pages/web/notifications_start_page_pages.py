from selene import browser, have
import allure


class NotificationsTitle:
    def open(self):
        with allure.step('Open site'):
            browser.open("/")

    def open_notifications(self):
        with allure.step('Open Notifications'):
            browser.element \
                ('[class="nbl-simpleControlButton nbl-simpleControlButton_size_quill nbl-simpleControlButton_style_mali"]') \
                .click()

    def assert_title(self):
        with allure.step('Text into notifications'):
            browser.element('[class="headerBar__title"]') \
                .should(have.text('Уведомления и акции'))


notifications_title = NotificationsTitle()
