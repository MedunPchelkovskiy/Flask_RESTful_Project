from flask import request
from flask_restful import Resource

from managers.authentication import auth
from managers.users import UserManager
from schemas.response.user import GetUserResponseSchema, UserUpdateResponseSchema


class UserResource(Resource):

    @staticmethod
    @auth.login_required
    def get(pk):
        user = UserManager.get_single_user(pk)
        return GetUserResponseSchema().dump(user)

    # Add decorator with roletype "admin". only admins can update user's role!
    @staticmethod
    @auth.login_required
    def put(pk):
        data = request.get_json()
        user = UserManager.get_user_to_update(pk)
        updated_user = UserManager.update_user_role(data, user)
        return UserUpdateResponseSchema().dump(updated_user), 201

    @staticmethod
    @auth.login_required
    def delete(pk):
        user = UserManager.get_single_user(pk)
        user_to_delete = UserManager.delete_user(user)

        return "User was successfully deleted"  # Try to replace "User" with name of the project(what i mean?!?)"
