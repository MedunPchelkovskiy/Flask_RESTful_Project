from marshmallow import Schema, fields, validate

from models.enums import Category


class BaseUserRequestSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)


class TopicBaseSchema(Schema):
    topic_name = fields.String(required=True)
    categorys = fields.Enum(Category, required=True)


class PostBaseSchema(Schema):
    text_of_post = fields.String(required=True)
    post_to_topic = fields.Integer(required=True)
