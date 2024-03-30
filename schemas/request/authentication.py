from marshmallow import fields, ValidationError, validate
from zxcvbn import zxcvbn

from models import UserModel
from schemas.base_schemas import BaseUserSchema


def check_password_strength(password):
    results = zxcvbn(password)
    if results["score"] > 3:
        pass
    else:
        raise ValidationError("Weak.Password must contain special characters")


def check_email_in_database(email):
    if UserModel.query.filter(UserModel.email == email).first():
        raise ValidationError('User with this email already exists')
    else:
        pass


def check_username_in_database(username):
    if UserModel.query.filter(UserModel.username == username).first():
        raise ValidationError('User with this username already exists')
    else:
        pass


class UserRegisterRequestSchema(BaseUserSchema):
    email = fields.Email(required=True,
                         validate=validate.And(check_email_in_database)
                         )
    password = fields.String(required=True,
                             validate=validate.And(validate.Length(min=9, max=42), check_password_strength)
                             )
    username = fields.String(min_length=2,
                             max_length=22,
                             required=True,
                             validate=validate.And(check_username_in_database, )
                             )


class UserLoginRequestSchema(BaseUserSchema):
    pass
