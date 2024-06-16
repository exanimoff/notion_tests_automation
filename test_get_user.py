import pytest
import allure
from client.users.get_user.model import GET_USER_RESPONSE_SCHEMA
from client.users.get_user.api import Users
from client.common.base_class import ResponseHandler

@pytest.mark.schemabased
@allure.feature("users")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a user returns expected results")
@allure.parent_suite("users")
@allure.suite("schemabased")
def test_get_user_schemabased(client):
    users = Users(client.NOTION_API_BASE_URL)
    user_id = client.USER_ID
    response = users.get_user(notion_api_token=client.NOTION_API_TOKEN, user_id=user_id)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(GET_USER_RESPONSE_SCHEMA, response.json())