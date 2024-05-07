import allure
from eyezon_project.pages.web.way_to_registration_form_page import registration_way


@allure.title('User going to the window registration')
def test_user_story_to_the_window_registration():
    registration_way.open()

    registration_way.auth_button_click()

    registration_way.registration_button_click()

    registration_way.assert_registration_window()
