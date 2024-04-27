import allure
from iVi_project.pages.web.search_recommendation_pages import search_recommendations


@allure.title('Checking title recommendations')
def test_search_title_recommandations():
    search_recommendations.open()

    search_recommendations.open_search_field()

    search_recommendations.assert_recommendation_title()
