from selene import browser, have
import allure


@allure.title('Check notifications text')
def test_notifications_text():
    with allure.step('Click notifications button'):
        browser.open('/')
        browser.element \
            ('[class="nbl-simpleControlButton nbl-simpleControlButton_size_quill nbl-simpleControlButton_style_mali"]') \
            .click()
    with allure.step('Text into notifications'):
        browser.element('[class="headerBar__title"]') \
            .should(have.text('Уведомления и акции'))
