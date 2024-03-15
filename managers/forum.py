from db import db
from managers.authentication import UserAuthManager, auth
from models import TopicModel, PostModel


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


class PostManager:

    @staticmethod
    def create_post(data):
        current_user = auth.current_user()
        data["post_author"] = current_user.username
        post = PostModel(**data)
        db.session.add(post)
        db.session.commit()
        return post

    @staticmethod
    def get_posts_for_topic(topic_pk):
        all_posts_for_topic = PostModel.query.filter_by(post_to_topic=topic_pk).all()
        return all_posts_for_topic
