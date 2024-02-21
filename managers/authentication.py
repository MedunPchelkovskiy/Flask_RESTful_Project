import datetime

import jwt
from decouple import config
from flask_bcrypt import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest

from db import db
from models.users import UserModel


class UserAuthManager:
    @staticmethod
    def create_user(data):
        password = data['password']
        data['password'] = generate_password_hash(password, 10).decode('utf8')
        user = UserModel(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def login_user(data):
        user = UserModel.query.filter_by(email=data['email']).first()
        if not user:
            raise BadRequest('Invalid email or password')

        if not check_password_hash(user.password, data['password']):
            raise BadRequest('Invalid email or password')
        return user

    @staticmethod
    def encode_auth_token(user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            token = jwt.encode(
                payload,
                config('SECRET_KEY'),
                algorithm='HS256'
            )
            return token
        except Exception as e:
            return e

    # @staticmethod
    # def decode_auth_token(auth_token):
    #     """
    #     Decodes the auth token
    #     :param auth_token:
    #     :return: integer|string
    #     """
    #     try:
    #         payload = jwt.decode(auth_token, config('SECRET_KEY'))
    #         return payload['sub']
    #     except jwt.ExpiredSignatureError:
    #         return 'Signature expired. Please log in again.'
    #     except jwt.InvalidTokenError:
    #         return 'Invalid token. Please log in again.'


