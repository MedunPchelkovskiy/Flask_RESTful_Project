import datetime

import jwt
from decouple import config
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_httpauth import HTTPTokenAuth
from itsdangerous import URLSafeTimedSerializer
from werkzeug.exceptions import BadRequest, Unauthorized

from db import db
from models.users import UserModel


class UserAuthManager:
    @staticmethod
    def create_user(data):
        password = data['password']
        data['password'] = generate_password_hash(password, 10).decode('utf8')
        user = UserModel(**data)
        # confirmed = False TODO: add after make migration for user model to update DB
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def login_user(data):
        user = UserModel.query.filter_by(email=data['email']).first()
        if not user:
            raise BadRequest('Please enter a valid email or password!')

        if not check_password_hash(user.password, data['password']):
            raise BadRequest('Please enter a valid email or password!')
        return user

    @staticmethod
    def encode_auth_token(user_id):
        try:
            payload = {
                'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=1),
                'iat': datetime.datetime.now(datetime.UTC),
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

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, key=config('SECRET_KEY'), algorithms=["HS256"])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    @staticmethod
    def generate_confirmation_token(email):
        serializer = URLSafeTimedSerializer(config['SECRET_KEY'])
        return serializer.dumps(email, salt=config['SECURITY_PASSWORD_SALT'])

    @staticmethod
    def decode_confirmation_token(token, expiration=3600):
        serializer = URLSafeTimedSerializer(config['SECRET_KEY'])
        try:
            email = serializer.loads(
                token,
                salt=config['SECURITY_PASSWORD_SALT'],
                max_age=expiration
            )
        except:
            return False
        return email

    @staticmethod
    def email_register_confirmation(token):             #TODO: think to use encode_auth_token to email confirmation process!!!!!!!!
        try:
            email = decode_confirmation_token(token)
        except:
            return 'The confirmation link is invalid or has expired.'
        user = UserModel.query.filter_by(email=email).first_or_404()
        if user.confirmed:
            return 'Account already confirmed. Please login.', 'success'
        else:
            user.confirmed = True
            user.confirmed_on = datetime.datetime.now()
            db.session.add(user)
            db.session.commit()
            return 'You have confirmed your account. Thanks!'


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    try:
        user_id = UserAuthManager.decode_auth_token(token)
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            raise Unauthorized('Invalid or missing token')
        return user
    except Exception as ex:
        raise Unauthorized('Invalid or missing token')
