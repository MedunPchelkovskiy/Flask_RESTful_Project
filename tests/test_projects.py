from managers.authentication import UserAuthManager
from models import RoleType
from tests.base_for_tests import TestBaseForApp
from tests.factory import ImageFactory, ProjectFactory, UserFactory


class TestProjectSchemas(TestBaseForApp):

    def test_missing_data_on_create_and_update_request_schema(self):
        user = UserFactory(role=RoleType.user)
        token = UserAuthManager.encode_auth_token(user.id)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        data = {}

        result = self.client.post("/projects", headers=headers, json=data)

        assert result.status_code == 400
        assert result.json == {
            "message": {
                "project_description": ["Missing data for required field."],
                "project_name": ["Missing data for required field."],
            }
        }

        project = ProjectFactory()
        image = ImageFactory()
        result = self.client.put("/project/0", headers=headers, json=data)

        assert result.status_code == 400
        assert result.json == {'message': {'_schema': ['At least one field is need to be filled.']}}
