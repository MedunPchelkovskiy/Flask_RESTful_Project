from db import db
from models import Topic, Post


class TopicManager:

    @staticmethod
    def create_topic(data):
        # current_user = ?
        # data["topic_author"] = current_user.id
        topic = Topic(**data)
        db.session.add(topic)
        db.session.commit()
        return topic


class PostManager:

    @staticmethod
    def create_post(data):
        # current_user = ?
        # data["topic_author"] = current_user.id
        post = Post(**data)
        db.session.add(post)
        db.session.commit()
        return post
