from flask import request
from flask_restful import Resource

from managers.authentication import auth
from managers.forum import TopicManager, PostManager
from models import TopicModel
from schemas.response.forum import CreateTopicResponseSchema, CreatePostResponseSchema, GetTopicWithPostsResponseSchema, \
    GetPostsResponseSchema, GetTopicsResponseSchema


class TopicsResource(Resource):

    @auth.login_required
    def post(self):
        data = request.get_json()
        topic = TopicManager.create_topic(data)
        return CreateTopicResponseSchema().dump(topic), 201

    def get(self):
        topics = TopicManager.get_all_topics()
        return GetTopicsResponseSchema(many=True).dump(topics)


class PostResource(Resource):

    @auth.login_required
    def post(self):
        data = request.get_json()
        post = PostManager.create_post(data)
        return CreatePostResponseSchema().dump(post), 201


class TopicResource(Resource):

    def get(self, pk):
        topic = TopicManager.get_topic(pk)
        return GetTopicWithPostsResponseSchema().dump(topic)

    def put(self):
        pass

    def delete(self):
        pass
