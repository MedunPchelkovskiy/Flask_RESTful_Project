from marshmallow import fields

from schemas.base_schemas import ProjectBaseSchema
from schemas.response.images import ImageResponseSchema


class CreateProjectResponseSchema(ProjectBaseSchema):
    id = fields.Integer(required=True)
    project_creation_date_time = fields.DateTime(required=True)
    project_author = fields.String(required=True)
    project_views_counter = fields.Integer(required=True)
    project_images = fields.List(fields.Nested(ImageResponseSchema))


class GetProjectWithImagesResponseSchema(CreateProjectResponseSchema):
    project_last_update_date_time = fields.DateTime(required=True)


class UpdateProjectResponseSchema(CreateProjectResponseSchema):
    project_last_update_date_time = fields.DateTime(required=True)
