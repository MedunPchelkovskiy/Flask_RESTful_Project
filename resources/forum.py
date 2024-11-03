from flask import request
from flask_restful import Resource

from helpers.decorators import validate_schema
from managers.authentication import auth
from managers.forum import PostManager, TopicManager
from schemas.request.forum import (CreatePostRequestSchema,
                                   CreateTopicRequestSchema)
from schemas.response.forum import (CreatePostResponseSchema,
                                    CreateTopicResponseSchema,
                                    EditPostResponseSchema,
                                    GetTopicsResponseSchema,
                                    GetTopicWithPostsResponseSchema)


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


class PostsResource(Resource):

    @validate_schema(CreatePostRequestSchema)
    @auth.login_required
    def post(self):
        data = request.get_json()
        post = PostManager.create_post(data)
        return CreatePostResponseSchema().dump(post), 201


class TopicResource(Resource):

    def get(self, pk):
        topic = TopicManager.get_single_topic(pk)
        return GetTopicWithPostsResponseSchema().dump(topic)

    def put(self):
        pass

    # only moderators can delete topics
    def delete(self):
        pass


class PostResource(Resource):

    @staticmethod
    @auth.login_required
    def put(pk):
        data = request.get_json()
        post = PostManager.get_single_post(pk)
        edited_post = PostManager.edit_post(post, data)
        return EditPostResponseSchema().dump(edited_post)

    @staticmethod
    @auth.login_required  # only moderators can delete posts, try to make it with decorator
    def delete(pk):
        post = PostManager.get_single_post(pk)
        post_for_delete = PostManager.delete_post(post)
        return "Post was deleted from moderator"
