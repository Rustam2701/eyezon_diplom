import allure
from eyezon_project.utils.api.base_request import base_request


@allure.title("User cannot register with invalid first name and last name")
def test_cannot_register_with_invalid_first_name_last_name(base_url):
    endpoint = "rest/users"
    payload = {"firstName": "dfghd", "lastName": "dfghdfg"}

    response = base_request(base_url=base_url, endpoint=endpoint, method="POST", json=payload)

    with allure.step('Status code=400'):
        assert response.status_code == 400


@allure.title("Check registration with invalid email")
def test_cannot_register_with_empty_email(base_url):
    endpoint = "rest/users"
    payload = {"firstName": "dfghd", "lastName": "dfghdfg", "email": ""}

    response = base_request(base_url=base_url, endpoint=endpoint, method="POST", json=payload)

    with allure.step('Status code=400 with response error "Bad Request"'):
        assert response.status_code == 400
        assert response.json()["error"] == "Bad Request"
