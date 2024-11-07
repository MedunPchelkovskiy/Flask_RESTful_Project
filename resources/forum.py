from flask import request
from flask_restful import Resource

from helpers.decorators import permission_checker, validate_schema
from managers.authentication import auth
from managers.forum import PostManager, TopicManager
from models import RoleType
from schemas.request.forum import (CreatePostRequestSchema,
                                   CreateTopicRequestSchema)
from schemas.response.forum import (CreatePostResponseSchema,
                                    CreateTopicResponseSchema,
                                    EditPostResponseSchema,
                                    GetTopicsResponseSchema,
                                    GetTopicWithPostsResponseSchema)


class TopicsResource(Resource):

    @auth.login_required
    @validate_schema(CreateTopicRequestSchema)
    def post(self):
        data = request.get_json()
        topic = TopicManager.create_topic(data)
        return CreateTopicResponseSchema().dump(topic), 201

    def get(self):
        topics = TopicManager.get_all_topics()
        return GetTopicsResponseSchema(many=True).dump(topics)


class TopicResource(Resource):

    @staticmethod
    def get(pk):
        topic = TopicManager.get_single_topic(pk)
        return GetTopicWithPostsResponseSchema().dump(topic)

    def put(self):  # TODO: make it not possible to update after few minutes from creating
        pass

    @staticmethod
    @auth.login_required
    @permission_checker(RoleType.moderator)
    def delete(pk):
        topic = TopicManager.get_single_topic(pk)
        project_to_delete = TopicManager.delete_topic(topic)


class PostsResource(Resource):

    @auth.login_required
    @validate_schema(CreatePostRequestSchema)
    def post(self):
        data = request.get_json()
        post = PostManager.create_post(data)
        return CreatePostResponseSchema().dump(post), 201


class PostResource(Resource):
    @staticmethod
    @auth.login_required
    def put(pk):
        data = request.get_json()
        post = PostManager.get_single_post(pk)
        edited_post = PostManager.edit_post(post, data)
        return EditPostResponseSchema().dump(edited_post)

    @staticmethod
    @auth.login_required
    @permission_checker(RoleType.moderator)
    def delete(pk):
        post = PostManager.get_single_post(pk)
        post_for_delete = PostManager.delete_post(post)
        return "Post was deleted from moderator"
