from werkzeug.exceptions import BadRequest

from db import db
from managers.authentication import auth
from models import UserModel


class UserManager:

    @staticmethod
    def get_single_user(user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            raise BadRequest("User with this id does not exist")
        db.session.commit()
        return user

    @staticmethod
    def get_user_to_update(user_id):
        user = UserModel.query.get(user_id)
        if not user:
            raise BadRequest("User with this id does not exist")
        return user

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
        return "User was successfully deleted"

    @staticmethod
    def update_user_role(data, user):
        if user.role != data["role"]:
            user.role = data["role"]
        db.session.commit()
        return user
