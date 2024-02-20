from marshmallow import fields

from schemas.base_schemas import BaseUserRequestSchema


class UserRegisterRequestSchema(BaseUserRequestSchema):
    username = fields.String(min_length=2, max_length=22, required=False)


class UserLoginRequestSchema(BaseUserRequestSchema):
    pass
