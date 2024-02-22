from flask import request
from flask_restful import Resource

from managers.forum import TopicManager
from schemas.response.forum import CreateTopicResponseSchema


class TopicsResource(Resource):

    def post(self):
        data = request.get_json()
        topic = TopicManager.create_topic(data)
        return CreateTopicResponseSchema().dump(topic), 201
