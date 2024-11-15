from flask import request
from flask_restful import Resource

from helpers.decorators import validate_schema
from helpers.sign_up_confirmation_via_email import UserRegisterMailConfirmation
from managers.authentication import UserAuthManager
from schemas.request.authentication import (UserLoginRequestSchema,
                                            UserRegisterRequestSchema)
from schemas.response.authentication import UserAuthenticationResponseSchema


class UserRegisterResource(Resource):
    @validate_schema(UserRegisterRequestSchema)
    def post(self):
        data = request.get_json()
        user = UserAuthManager.create_user(data)
        token = UserAuthManager.encode_auth_token(user.id)
        return UserAuthenticationResponseSchema().dump({"token": token}), 201


class UserRegisterEmailConfirmationResource(Resource):
    @staticmethod
    def get(token):  # method make sense to be "post" !?!?!?!
        UserRegisterMailConfirmation.confirm_email(token)
        return "You have confirmed your account. Thanks!", 201


class UserLoginResource(Resource):
    @validate_schema(UserLoginRequestSchema)
    def post(self):
        data = request.get_json()
        user = UserAuthManager.login_user(data)
        token = UserAuthManager.encode_auth_token(user.id)
        return UserAuthenticationResponseSchema().dump({"token": token}), 201
