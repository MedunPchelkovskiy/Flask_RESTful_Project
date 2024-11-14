from unittest.mock import patch

from helpers.sign_up_confirmation_via_email import EmailSending
from models import UserModel
from tests.base_for_tests import TestBaseForApp


class TestUsers(TestBaseForApp):

    # @patch.object(gmail_api_services, "send_message", return_value="test_link_for_confirmation")
    @patch.object(EmailSending, "send_email", return_value=None)
    def test_create_user(self, mock_email_sending):
        user = UserModel.query.all()
        assert len(user) == 0
        data = {"email": "test@mail.com",
                "password": "MySuper#4@SeCurE_PasswoRd",
                "username": "Samadhi"}

        result = self.client.post("/signup", json=data)

        assert result.status_code == 201
        user = UserModel.query.all()
        assert len(user) == 1
