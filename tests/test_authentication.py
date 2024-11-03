from tests.base_for_tests import TestBaseForApp


class TestOnlyAuthenticatedUsers(TestBaseForApp):
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