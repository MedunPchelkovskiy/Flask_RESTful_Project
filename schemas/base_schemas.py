from marshmallow import Schema, fields, validate, ValidationError
from zxcvbn import zxcvbn
from models import UserModel


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


class BaseUserRequestSchema(Schema):
    email = fields.Email(required=True,
                         validate=validate.And(check_email_in_database)
                         )
    password = fields.String(required=True,
                             validate=validate.And(validate.Length(min=9, max=42), check_password_strength)
                             )


class ComplaintBaseSchema(Schema):
    title = fields.String(requred=True)
    description = fields.String(requred=True)
    amount = fields.Float(requred=True)
    photo = fields.String()
    photo_extension = fields.String()
