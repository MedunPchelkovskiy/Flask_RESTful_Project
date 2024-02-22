from marshmallow import Schema, fields

from models.enums import Category


class CreateTopicResponseSchema(Schema):
    id = fields.Integer(required=True)
    topic_name = fields.String(required=True)
    categorys = fields.Enum(Category, by_value=True)
    topic_creation_date_time = fields.DateTime(required=True)
    topic_author = fields.Integer(required=True)
