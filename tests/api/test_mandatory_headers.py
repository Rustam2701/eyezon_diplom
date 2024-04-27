import allure
from iVi_project.utils.api.base_request import base_request


@allure.title("")
def test_cannot_send_request_without_mandatory_headers(base_url):
    endpoint = "pivi/rabbi.AuthHelpers/Validate"
    payload = {"value": "test@mail"}

    response = base_request(base_url=base_url, endpoint=endpoint, method="POST", json=payload)

    with allure.step('Status code=400'):
        assert response.status_code == 412

    with allure.step('Status code=400'):
        assert response.json()['message'] == 'app_version is required'
