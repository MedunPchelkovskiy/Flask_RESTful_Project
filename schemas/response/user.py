from marshmallow import fields

from schemas.base_schemas import BaseUserSchema
from schemas.response.projects import GetProjectWithImagesResponseSchema


class GetUserResponseSchema(BaseUserSchema):
    id = fields.Integer(required=True)
    username = fields.String(required=True)
    role = fields.String(required=True)
    projects = fields.List(fields.Nested(GetProjectWithImagesResponseSchema))


class UserUpdateResponseSchema(GetUserResponseSchema):
    pass
