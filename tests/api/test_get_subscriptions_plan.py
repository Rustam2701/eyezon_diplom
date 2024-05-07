import allure
from jsonschema import validate
from eyezon_project.utils.api.base_request import base_request
from eyezon_project.schemas.subscriptions_plan_schema import subscription_plans


@allure.title("Check list of subscription return for new users")
def test_can_get_list_of_subscriptions(base_url):
    endpoint = "payments/subscription-plans"

    response = base_request(base_url=base_url, endpoint=endpoint, method="GET")

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('Schema is validate'):
        validate(response.json(), subscription_plans)
