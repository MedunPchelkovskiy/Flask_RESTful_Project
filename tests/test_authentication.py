from managers.authentication import UserAuthManager
from models import RoleType
from tests.base_for_tests import TestBaseForApp
from tests.factory import (ImageFactory, PostFactory, ProjectFactory,
                           TopicFactory, UserFactory)


class TestOnlyAuthenticatedUsersAccess(TestBaseForApp):
    def test_user_is_authenticated(self):
        protected_urls = [
            ("POST", "/projects"),
            ("GET", "/project/17"),
            ("PUT", "/project/17"),
            ("DELETE", "/project/17"),
        ]

        for method, url in protected_urls:
            if method == "POST":
                result = self.client.post(url)
            elif method == "GET":
                result = self.client.get(url)
            elif method == "PUT":
                result = self.client.put(url)
            elif method == "DELETE":
                result = self.client.delete(url)

            assert result.status_code == 401
            assert result.json == {"message": "Invalid, expired or missing token"}

    def test_user_have_permission(self):
        user = UserFactory(role=RoleType.user)
        token = UserAuthManager.encode_auth_token(user.id)
        headers = {"Authorization": f"Bearer {token}"}

        result = self.client.delete("/post/6", headers=headers)
        assert result.status_code == 403
        assert result.json == {"message": "You must have permission to do this!"}

        user = UserFactory(role=RoleType.moderator)
        post = PostFactory()
        topic = TopicFactory()
        token = UserAuthManager.encode_auth_token(user.id)
        headers = {"Authorization": f"Bearer {token}"}

        result = self.client.delete("/post/0", headers=headers)
        assert result.status_code == 200
        assert result.json == "Post was deleted from moderator"
