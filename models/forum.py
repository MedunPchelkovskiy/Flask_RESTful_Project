from datetime import datetime

from db import db
from models.enums import Category


class Topic(db.Model):
    __tablename__ = 'topic'

    id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(255), nullable=False)
    categorys = db.Column(db.Enum(Category), nullable=False)
    topic_creation_date_time = db.Column(db.DateTime, default=datetime.utcnow())
    topic_author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    text_of_post = db.Column(db.Text, nullable=False)
    date_time_of_post = db.Column(db.DateTime, default=datetime.utcnow())
    post_to_topic = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False)
    post_author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
