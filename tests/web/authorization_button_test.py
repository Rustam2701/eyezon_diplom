from selene import browser
import allure


@allure.title("Authorization button clickable")
def test_clickable_auth_button():
    with allure.step('Open site'):
        browser.open('/')

    with allure.step('Click Authorization22 button'):
        browser.element('[data-test=header_avatar]').click()
