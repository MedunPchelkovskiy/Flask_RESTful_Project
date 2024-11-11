from marshmallow import Schema, fields

from schemas.base_schemas import PostBaseSchema, TopicBaseSchema


class CreateTopicResponseSchema(TopicBaseSchema):
    id = fields.Integer(required=True)
    topic_creation_date_time = fields.DateTime(required=True)
    topic_author = fields.String(required=True)


class CreatePostResponseSchema(PostBaseSchema):
    # id = fields.Integer(required=True)
    date_time_of_create_post = fields.DateTime(required=True)
    date_time_of_update_post = fields.DateTime(required=True)
    post_author = fields.String(required=True)
    # post_to_topic = fields.Integer(required=True)


class GetTopicsResponseSchema(CreateTopicResponseSchema):
    pass


class GetPostsResponseSchema(CreatePostResponseSchema):
    pass


class EditPostResponseSchema(CreatePostResponseSchema):
    date_time_of_update_post = fields.DateTime(required=True)


class EditTopicResponseSchema(CreateTopicResponseSchema):
    topic_last_update_date_time = fields.DateTime(required=True)


class GetTopicWithPostsResponseSchema(CreateTopicResponseSchema):
    topic_last_update_date_time = fields.DateTime(required=True)
    posts = fields.List(fields.Nested(CreatePostResponseSchema))
