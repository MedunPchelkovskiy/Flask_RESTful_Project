from flask import request
from flask_restful import Resource

from managers.forum import TopicManager, PostManager
from schemas.response.forum import CreateTopicResponseSchema, CreatePostResponseSchema


class TopicsResource(Resource):

    def post(self):
        data = request.get_json()
        topic = TopicManager.create_topic(data)
        return CreateTopicResponseSchema().dump(topic), 201


class PostResource(Resource):

    def post(self):
        data = request.get_json()
        post = PostManager.create_post(data)
        return CreatePostResponseSchema().dump(post), 201
