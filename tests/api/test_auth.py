import allure
from eyezon_project.utils.api.base_request import base_request


@allure.title("Check auth with invalid password")
def test_cannot_auth_with_invalid_password(base_url):
    endpoint = "auth/login"
    payload = {"username": "test@test.com", "password": "123123"}

    response = base_request(base_url=base_url, endpoint=endpoint, method="POST", json=payload)

    with allure.step('Status code=400'):
        assert response.status_code == 401
        assert response.json()['message'] == 'wrong_pass'
        assert response.json()['error'] == 'Unauthorized'


@allure.title("Check auth with invalid email")
def test_cannot_auth_with_invalid_email(base_url):
    endpoint = "auth/login"
    payload = {"username": "test@", "password": "123123"}

    response = base_request(base_url=base_url, endpoint=endpoint, method="POST", json=payload)

    with allure.step('Status code=400'):
        assert response.status_code == 401
        assert response.json()['error'] == 'Unauthorized'


@allure.title("Check auth without mandatory field")
def test_cannot_auth_without_mandatory_field(base_url):
    endpoint = "auth/login"

    response = base_request(base_url=base_url, endpoint=endpoint, method="POST", json={})

    with allure.step('Status code=400'):
        assert response.status_code == 401
