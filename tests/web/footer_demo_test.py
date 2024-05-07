import allure
from eyezon_project.pages.web.footer_demo_page import demo_footer


@allure.title('User see footer section DEMO')
def test_footer_demo():
    demo_footer.open()
    
    demo_footer.click_demo_button()

    demo_footer.assert_demo_section_in_footer()
