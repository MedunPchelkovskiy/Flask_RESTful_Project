from unittest.mock import patch

from managers.authentication import UserAuthManager
from models import RoleType, ProjectModel, ImageModel
from serices.cloudinary_services import ImagesOnCloud
from tests.base_for_tests import TestBaseForApp
from tests.factory import UserFactory, ProjectFactory
from tests.helpers import converted_image


class TestProjectSchemas(TestBaseForApp):

    def test_missing_data_on_create_request_schema(self):
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

    @patch.object(ImagesOnCloud, "get_asset_info", return_value="image_on_cloud_url")
    @patch.object(ImagesOnCloud, "upload_image", return_value=None)
    def test_create_and_update_project_with_photo_upload(
        self, mock_cloudinary_upload, mock_get_asset_info
    ):
        projects = ProjectModel.query.all()
        assert len(projects) == 0

        images = ImageModel.query.all()
        assert len(images) == 0

        user = UserFactory(role=RoleType.user)
        token = UserAuthManager.encode_auth_token(user.id)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        data = {
            "project_name": "Test Project",
            "project_description": "Description for test project",
            "project_images": converted_image,
        }

        result = self.client.post("/projects", headers=headers, json=data)

        assert result.status_code == 201
        projects = ProjectModel.query.all()
        assert len(projects) == 1

        images = ImageModel.query.all()
        assert len(images) == 1

        data = {}

        result = self.client.put("/project/0", headers=headers, json=data)

        assert result.status_code == 400
        assert result.json == {
            "message": {"_schema": ["At least one field is need to be filled."]}
        }


class TestProjectCreateAndUpdateMethods(TestBaseForApp):

    def test_update_project(self):
        user = UserFactory(role=RoleType.user)
        project = ProjectFactory()
        token = UserAuthManager.encode_auth_token(user.id)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        projects = ProjectModel.query.all()
        assert len(projects) == 1

        data = {"project_description": "Description for test project"}

        result = self.client.put("/project/0", headers=headers, json=data)

        assert result.status_code == 201
