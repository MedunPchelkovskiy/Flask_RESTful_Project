from flask import request
from flask_restful import Resource

from helpers.decorators import validate_schema
from managers.authentication import auth
from managers.forum import TopicManager, PostManager
from schemas.request.forum import CreateTopicRequestSchema, CreatePostRequestSchema
from schemas.response.forum import CreateTopicResponseSchema, CreatePostResponseSchema, \
    GetTopicWithPostsResponseSchema, GetTopicsResponseSchema


class TopicsResource(Resource):

    @validate_schema(CreateTopicRequestSchema)
    @auth.login_required
    def post(self):
        data = request.get_json()
        topic = TopicManager.create_topic(data)
        return CreateTopicResponseSchema().dump(topic), 201

    def get(self):
        topics = TopicManager.get_all_topics()
        return GetTopicsResponseSchema(many=True).dump(topics)


class PostResource(Resource):

    @validate_schema(CreatePostRequestSchema)
    @auth.login_required
    def post(self):
        data = request.get_json()
        post = PostManager.create_post(data)
        return CreatePostResponseSchema().dump(post), 201

    def put(self):
        pass

    # only moderators can delete posts
    def delete(self):
        pass


class TopicResource(Resource):

    def get(self, pk):
        topic = TopicManager.get_single_topic(pk)
        return GetTopicWithPostsResponseSchema().dump(topic)

    def put(self):
        pass

    # only moderators can delete topics
    def delete(self):
        pass
