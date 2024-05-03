import allure
from eyezon_project.pages.web.checking_main_fields_in_registration_window_page import free_subscription_title


@allure.title('Free watching subscription title correct')
def test_visible_free_watching_button():
    free_subscription_title.open()

    free_subscription_title.auth_button_click11()

    free_subscription_title.registration_button_click22()

    free_subscription_title.click_button_next()

    free_subscription_title.assert_notifications_about_required_fields()
