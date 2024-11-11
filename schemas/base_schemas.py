from marshmallow import Schema, fields

from models.enums import Category


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)


class TopicBaseSchema(Schema):
    topic_name = fields.String(required=True)
    categorys = fields.Enum(Category, required=True)


class PostBaseSchema(Schema):
    text_of_post = fields.String(required=True)


class ProjectBaseSchema(Schema):
    project_name = fields.String(required=True)
    project_description = fields.String(required=True)
    project_images = fields.String(required=False)


class ImagesBaseSchema(Schema):
    # id = fields.Integer(required=True)
    image_url = fields.String(required=True)
    image_uploading_date_time = fields.DateTime(required=True)
