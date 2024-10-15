from werkzeug.security import generate_password_hash

from db import db
from models import UserModel, RoleType


def create_super_user(email, password, username):
    password = generate_password_hash(password)
    user = UserModel(
        email=email,
        password=password,
        username=username,
        role=RoleType.admin,
    )
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    create_super_user("superuser@email.com", "superpassword", "TheDude")
