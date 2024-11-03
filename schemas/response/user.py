from marshmallow import Schema, fields

from schemas.response.projects import GetProjectWithImagesResponseSchema


class GetUserResponseSchema(Schema):
    id = fields.Integer(required=True)
    username = fields.String(required=True)
    role = fields.String(required=True)
    projects = fields.List(fields.Nested(GetProjectWithImagesResponseSchema))


class UserUpdateResponseSchema(GetUserResponseSchema):
    pass
