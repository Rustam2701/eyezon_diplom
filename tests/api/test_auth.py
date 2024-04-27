import allure
from iVi_project.data.base_requests_headers import headers
from iVi_project.utils.api.base_request import base_request


@allure.title("Check auth with invalid mail")
def test_cannot_auth_with_invalid_email(base_url):
    endpoint = "pivi/rabbi.AuthHelpers/Validate"
    payload = {"value": "test@mail"}

    response = base_request(base_url=base_url, endpoint=endpoint, method="POST", json=payload, headers=headers)

    with allure.step('Status code=400'):
        assert response.status_code == 400

    print(response.json())
