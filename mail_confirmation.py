from datetime import datetime, timezone

from decouple import config
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer

from db import db
from models import UserModel


class UserRegisterMailConfirmation:

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
    def send_email(to, subject, template):
        msg = Message(
            subject,
            recipients=[to],
            html=template,
            sender=config['MAIL_DEFAULT_SENDER']
        )
        mail.send(msg)

    @staticmethod
    def confirm_email(token):
        try:
            email = UserRegisterMailConfirmation.decode_confirmation_token(token)
        except:
            return 'The confirmation link is invalid or has expired.'
        user = UserModel.query.filter_by(email=email).first_or_404()
        if user.confirmed:
            return 'Account already confirmed. Please login.'
        else:
            user.confirmed = True
            user.confirmed_on = datetime.now(timezone.utc)
            db.session.add(user)
            db.session.commit()
            return 'You have confirmed your account. Thanks!'
        # return redirect(url_for('main.home'))

    @staticmethod
    def email_register_confirmation(token):
        try:
            email = UserRegisterMailConfirmation.decode_confirmation_token(token)
        except:
            return 'The confirmation link is invalid or has expired.'
        user = UserModel.query.filter_by(email=email).first_or_404()
        if user.confirmed:
            return 'Account already confirmed. Please login.', 'success'
        else:
            user.confirmed = True
            user.confirmed_on = datetime.now(timezone.utc)
            db.session.add(user)
            db.session.commit()
            return 'You have confirmed your account. Thanks!'
