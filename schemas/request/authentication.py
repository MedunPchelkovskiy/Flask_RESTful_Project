from marshmallow import fields, ValidationError, validate

from models import UserModel
from schemas.base_schemas import BaseUserRequestSchema


def check_username_in_database(username):
    if UserModel.query.filter(UserModel.username == username).first():
        raise ValidationError('User with this username already exists')
    else:
        pass


class UserRegisterRequestSchema(BaseUserRequestSchema):
    username = fields.String(min_length=2,
                             max_length=22,
                             required=True,
                             validate=validate.And(check_username_in_database)
                             )


class UserLoginRequestSchema(BaseUserRequestSchema):
    pass
