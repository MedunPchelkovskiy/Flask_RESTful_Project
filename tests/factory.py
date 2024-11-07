from datetime import datetime

import factory
from db import db
from models import UserModel, RoleType


class FactoryBase(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


class UserFactory(FactoryBase):
    class Meta:
        model = UserModel

    id = factory.Sequence(lambda n: n)
    email = factory.Faker("email")
    password = factory.Faker("password")
    username = factory.Faker("user_name")
    registered_at = datetime.utcnow()  # now(timezone.utc)
    confirmed = False
    role = RoleType.user