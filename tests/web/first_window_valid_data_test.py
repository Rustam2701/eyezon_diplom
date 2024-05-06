import allure
from eyezon_project.pages.web.first_window_valid_data_page import first_page_valid_data


@allure.title('Valid data first page registration')
def test_first_window_valid_data():
    first_page_valid_data.open()

    first_page_valid_data.auth_button_click()

    first_page_valid_data.registration_button_click()

    first_page_valid_data.type_first_name()

    first_page_valid_data.type_last_name()

    first_page_valid_data.check_country()

    first_page_valid_data.click_submit_button()

    first_page_valid_data.assert_second_window_registration()
