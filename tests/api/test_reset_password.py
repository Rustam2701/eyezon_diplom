import allure
from eyezon_project.utils.api.base_request import base_request


@allure.title("Check user can request email for new password")
def test_can_reset_password():
    base_url = 'https://serverru.eyezon.online/api/'
    endpoint = "user/reset"
    payload = {"email": "test@test.com"}

    response = base_request(base_url=base_url, endpoint=endpoint, method="POST", json=payload)

    with allure.step('Status code=200'):
        assert response.status_code == 200
