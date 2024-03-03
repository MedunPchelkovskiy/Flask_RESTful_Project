from marshmallow import Schema, fields

from models.enums import Category


class CreateTopicResponseSchema(Schema):
    id = fields.Integer(required=True)
    topic_name = fields.String(required=True)
    categorys = fields.Enum(Category, by_value=True)
    topic_creation_date_time = fields.DateTime(required=True)
    topic_author = fields.String(required=True)


class CreatePostResponseSchema(Schema):
    id = fields.Integer(required=True)
    text_of_post = fields.String(required=True)
    topic_creation_date_time = fields.DateTime(required=True)
    post_to_topic = fields.Integer(required=True)
    post_author = fields.String(required=True)


class GetTopicsResponseSchema(CreateTopicResponseSchema):
    pass

class GetPostsResponseSchema(CreatePostResponseSchema):
    pass


class GetTopicWithPostsResponseSchema(CreateTopicResponseSchema):
    posts = fields.List(fields.Nested(CreatePostResponseSchema))




