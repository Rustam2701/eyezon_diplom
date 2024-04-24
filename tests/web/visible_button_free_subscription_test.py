import allure
from iVi_tests.pages.web.visible_button_free_subscription import free_subscription_title


@allure.title('Visible button of free watching subscription in start page')
def test_visible_free_watching_button():
    free_subscription_title.open()

    free_subscription_title.open_catalog_films()

    free_subscription_title.open_page_with_free_subscription()

    free_subscription_title.assert_text_in_free_subscription()
