import allure
from iVi_project.pages.web.catalog_content_pages import catalog_content


@allure.title('Catalog "Мультфильмы" contents')
def test_catalog_has_cartoons():
    catalog_content.open()

    catalog_content.open_catalog()

    catalog_content.assert_text_cartoon()
