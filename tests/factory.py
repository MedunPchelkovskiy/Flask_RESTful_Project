from datetime import datetime

import factory
from factory import RelatedFactoryList, SelfAttribute, SubFactory

from db import db
from models import (Category, ImageModel, PostModel, ProjectModel, RoleType,
                    TopicModel, UserModel)


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


class ProjectFactory(FactoryBase):
    class Meta:
        model = ProjectModel

    id = factory.Sequence(lambda n: n)
    project_name = factory.Faker("user_name")
    project_description = factory.Faker("text")
    project_creation_date_time = factory.Faker("date_time")
    project_last_update_date_time = factory.Faker("date_time")
    project_views_counter = factory.Sequence(lambda n: n)
    project_author = 0  # factory.Sequence(lambda n: n)
    project_images = RelatedFactoryList(
        "tests.factory.ImageFactory", size=1, id=SelfAttribute("..id")
    )


class ImageFactory(FactoryBase):
    class Meta:
        model = ImageModel

    id = factory.Sequence(lambda n: n)
    image_url = factory.Faker("text")
    image_uploading_date_time = factory.Faker("date_time")
    image_to_project = factory.Sequence(lambda n: n)
    project = SubFactory(ProjectFactory, project_images=[])


class TopicFactory(FactoryBase):
    class Meta:
        model = TopicModel

    id = factory.Sequence(lambda n: n)
    topic_name = factory.Faker("user_name")
    categorys = Category.paintings
    topic_creation_date_time = factory.Faker("date_time")
    topic_last_update_date_time = factory.Faker("date_time")
    topic_author = factory.Faker("user_name")
    posts = RelatedFactoryList(
        "tests.factory.PostFactory", size=1, id=SelfAttribute("..id")
    )


class PostFactory(FactoryBase):
    class Meta:
        model = PostModel

    id = factory.Sequence(lambda n: n)
    text_of_post = factory.Faker("text")
    date_time_of_create_post = factory.Faker("date_time")
    date_time_of_update_post = factory.Faker("date_time")
    post_author = factory.Faker("user_name")
    post_to_topic = factory.Sequence(lambda n: n)
    topic = SubFactory(TopicFactory, posts=[])
