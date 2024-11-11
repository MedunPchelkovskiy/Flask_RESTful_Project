from marshmallow import Schema, ValidationError, fields, validates_schema

from helpers.decorators import validate_schema
from schemas.base_schemas import ProjectBaseSchema


class CreateProjectRequestSchema(ProjectBaseSchema):
    pass


class UpdateProjectRequestSchema(Schema):
    project_description = fields.String(required=False)
    project_images = fields.String(required=False)

    @validates_schema
    def fill_at_least_one_field(self, data):
        if "project_description" not in data and "project_images" not in data:
            raise ValidationError("At least one field is need to be filled.")
