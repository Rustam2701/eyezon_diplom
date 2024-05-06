import allure
from eyezon_project.pages.web.going_to_the_registration_window_page import search_recommendations


@allure.title('User going to the window registration')
def test_user_story_to_the_window_registration():
    search_recommendations.open()

    search_recommendations.auth_button_click()

    search_recommendations.registration_button_click()

    search_recommendations.assert_registration_window()
