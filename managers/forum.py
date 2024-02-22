from db import db
from models import Topic


class TopicManager:

    @staticmethod
    def create_topic(data):
        # current_user = ?
        # data["topic_author"] = current_user.id
        topic = Topic(**data)
        db.session.add(topic)
        db.session.commit()
        return topic
