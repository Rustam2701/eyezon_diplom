import allure
from iVi_project.pages.web.notifications_start_page_pages import notifications_title


@allure.title('Check notifications text')
def test_notifications_text():
    notifications_title.open()

    notifications_title.open_notifications()

    notifications_title.assert_title()
