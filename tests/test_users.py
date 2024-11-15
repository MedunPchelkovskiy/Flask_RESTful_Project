from unittest.mock import patch

from helpers.sign_up_confirmation_via_email import EmailSending
from helpers.sign_up_confirmation_via_email import UserRegisterMailConfirmation
from managers.authentication import UserAuthManager
from models import UserModel
from tests.base_for_tests import TestBaseForApp
from tests.helpers import encoded_token


class TestUsers(TestBaseForApp):

    @patch.object(UserAuthManager, "encode_auth_token", return_value=encoded_token)
    @patch.object(EmailSending, "send_email", return_value="Some confirmation link")
    def test_create_user(self, mock_email_sending, mock_encode_auth_token):
        users = UserModel.query.all()
        assert len(users) == 0
        data = {
            "email": "test@mail.com",
            "password": "MySuper#4@SeCurE_PasswoRd",
            "username": "Samadhi",
        }

        result = self.client.post("/signup", json=data)

        assert result.status_code == 201
        assert result.json == {"token": encoded_token}
        users = UserModel.query.all()
        assert len(users) == 1
        assert users[0].confirmed == False

        token = UserAuthManager.encode_auth_token(users[0].id)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        email = users[0].email
        confirmation_token = UserRegisterMailConfirmation.generate_confirmation_token(email)
        url = f"/confirm/{confirmation_token}"

        result = self.client.get(url, headers=headers)

        assert result.status_code == 201
        assert users[0].confirmed == True
