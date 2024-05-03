import allure
from eyezon_project.pages.web.going_to_the_registration_window_page import search_recommendations


@allure.title('Checking title recommendations')
def test_search_title_recommandations():
    search_recommendations.open()

    search_recommendations.auth_button_click()

    search_recommendations.registration_button_click()

    search_recommendations.assert_registration_window()
