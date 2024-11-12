from datetime import datetime, timezone

from decouple import config
from flask import render_template, url_for
from itsdangerous import URLSafeTimedSerializer

from db import db
from models import UserModel
from serices.gmail_api_services import (create_message, gmail_authenticate,
                                        send_message)


class UserRegisterMailConfirmation:

    @staticmethod
    def generate_confirmation_token(email):
        serializer = URLSafeTimedSerializer(config("SECRET_KEY"))
        return serializer.dumps(email, salt=config("SECURITY_PASSWORD_SALT"))

    @staticmethod
    def decode_confirmation_token(token, expiration=3600):
        serializer = URLSafeTimedSerializer(config("SECRET_KEY"))
        try:
            email = serializer.loads(
                token, salt=config("SECURITY_PASSWORD_SALT"), max_age=expiration
            )
        except:
            return False
        return email

    @staticmethod
    def confirm_email(token):
        try:
            email = UserRegisterMailConfirmation.decode_confirmation_token(token)
        except:
            return "The confirmation link is invalid or has expired."
        user = UserModel.query.filter_by(email=email).first_or_404()
        if user.confirmed:
            return "Account already confirmed. Please login."
        else:
            user.confirmed = True
            user.confirmed_on = datetime.now(timezone.utc)
            db.session.add(user)
            db.session.commit()
            return "You have confirmed your account. Thanks!"
        # return redirect(url_for('main.home'))

    @staticmethod
    def email_register_confirmation(token):
        try:
            email = UserRegisterMailConfirmation.decode_confirmation_token(token)
        except:
            return "The confirmation link is invalid or has expired."
        user = UserModel.query.filter_by(email=email).first()
        if user.confirmed:
            return "Account already confirmed. Please login.", "success"
        else:
            user.confirmed = True
            user.confirmed_on = datetime.now(timezone.utc)
            db.session.add(user)
            db.session.commit()
            return "You have confirmed your account. Thanks!"

class EmailSending:

    @staticmethod
    def send_email(email):
        confirmation_token = UserRegisterMailConfirmation.generate_confirmation_token(email)
        confirm_url = url_for(
            "userregisteremailconfirmationresource",
            token=confirmation_token,
            _external=True,
        )
        html = render_template("base_email_template.html", confirm_url=confirm_url)
        subject = "Please confirm your email"
        message = create_message(
            sender=config("MAIL_DEFAULT_SENDER"),
            to=email,
            subject=subject,
            message_text=html,
        )
        service = gmail_authenticate()
        send_message(service, message)
