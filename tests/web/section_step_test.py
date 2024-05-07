import allure
from eyezon_project.pages.web.section_step_page import how_it_works


@allure.title('User can see section "How it works"')
def test_step_to_section_how_it_works():
    how_it_works.open()

    how_it_works.click_button_how_it_works()

    how_it_works.assert_title_section_how_it_works()
