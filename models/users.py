from db import db
from models.enums import RoleType


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=True, unique=True)
    # confirmed = db.Column(db.Boolean, nullable=False, default=False)         TODO: add for email confirmation when new user register
    role = db.Column(db.Enum(RoleType), default=RoleType.user, nullable=False)
    projects = db.relationship('ProjectModel', backref='project', lazy='dynamic')
