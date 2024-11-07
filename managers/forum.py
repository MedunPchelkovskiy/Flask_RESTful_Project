from datetime import datetime, timedelta

from werkzeug.exceptions import BadRequest, Unauthorized

from db import db
from managers.authentication import auth
from models import PostModel, RoleType, TopicModel


class TopicManager:

    @staticmethod
    def create_topic(data):
        current_user = auth.current_user()
        data["topic_author"] = current_user.username
        topic = TopicModel(**data)
        db.session.add(topic)
        db.session.commit()
        return topic

    @staticmethod
    def get_single_topic(topic_id):
        topic = TopicModel.query.filter_by(id=topic_id).first()
        return topic

    @staticmethod
    def get_all_topics():
        topics = TopicModel.query.all()
        return topics

    @staticmethod
    def delete_topic(topic):
        db.session.delete(topic)
        db.session.commit()
        return


class PostManager:

    @staticmethod
    def create_post(data):
        current_user = auth.current_user()
        data["post_author"] = current_user.username
        post = PostModel(**data)
        current_topic = TopicManager.get_single_topic(post.post_to_topic)
        current_topic.topic_last_update_date_time = datetime.utcnow()
        db.session.add(post)
        db.session.commit()
        return post

    @staticmethod
    def get_posts_for_topic(topic_pk):
        all_posts_for_topic = PostModel.query.filter_by(post_to_topic=topic_pk).all()
        return all_posts_for_topic

    @staticmethod
    def get_single_post(post_id):
        post = PostModel.query.get(post_id)
        if not post:
            raise BadRequest("Post with this id does not exist")
        return post

    @staticmethod
    def delete_post(post):
        # current_user = auth.current_user()
        # if current_user.role == RoleType.moderator:
        db.session.delete(post)
        db.session.commit()
        # else:
        #     raise Unauthorized("You have no permission")

    @staticmethod
    def edit_post(post, data):
        current_user = auth.current_user()
        if not current_user.username == post.post_author:
            raise Unauthorized("You have no permission")
        if datetime.utcnow().timestamp() - post.date_time_of_create_post.timestamp() > 360:
            return "Time to update is end!"
        else:
            post.text_of_post = data["text_of_post"]
            post.date_time_of_update_post = datetime.utcnow()
            current_topic = TopicManager.get_single_topic(post.post_to_topic)
            current_topic.topic_last_update_date_time = datetime.utcnow()
            db.session.commit()
        return post
