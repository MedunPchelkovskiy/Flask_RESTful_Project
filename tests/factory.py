from datetime import datetime

from factory import (Factory, Faker, RelatedFactoryList, SelfAttribute,
                     Sequence, SubFactory)

from db import db
from models import (Category, ImageModel, PostModel, ProjectModel, RoleType,
                    TopicModel, UserModel)


class FactoryBase(Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


class UserFactory(FactoryBase):
    class Meta:
        model = UserModel

    id = Sequence(lambda n: n)
    email = Faker("email")
    password = Faker("password")
    username = Faker("user_name")
    registered_at = datetime.utcnow()  # now(timezone.utc)
    confirmed = False
    role = RoleType.user


def get_user_id():
    return UserFactory().id


class ProjectFactory(FactoryBase):
    class Meta:
        model = ProjectModel

    id = Sequence(lambda n: n)
    project_name = Faker("user_name")
    project_description = Faker("text")
    project_creation_date_time = Faker("date_time")
    project_last_update_date_time = Faker("date_time")
    project_views_counter = Sequence(lambda n: n)
    project_author = 0  # TODO: make it with "LazyFunction", to get user.id when need it ; factory.LazyFunction(get_user_id)
    project_images = RelatedFactoryList(
        "tests.factory.ImageFactory", size=1, id=SelfAttribute("..id")
    )


class ImageFactory(FactoryBase):
    class Meta:
        model = ImageModel

    id = Sequence(lambda n: n)
    image_url = Faker("text")
    image_uploading_date_time = Faker("date_time")
    image_to_project = Sequence(lambda n: n)
    project = SubFactory(ProjectFactory, project_images=[])


class TopicFactory(FactoryBase):
    class Meta:
        model = TopicModel

    id = Sequence(lambda n: n)
    topic_name = Faker("user_name")
    categorys = Category.paintings
    topic_creation_date_time = Faker("date_time")
    topic_last_update_date_time = Faker("date_time")
    topic_author = Faker("user_name")
    posts = RelatedFactoryList(
        "tests.factory.PostFactory", size=1, id=SelfAttribute("..id")
    )


class PostFactory(FactoryBase):
    class Meta:
        model = PostModel

    id = Sequence(lambda n: n)
    text_of_post = Faker("text")
    date_time_of_create_post = Faker("date_time")
    date_time_of_update_post = Faker("date_time")
    post_author = Faker("user_name")
    post_to_topic = Sequence(lambda n: n)
    topic = SubFactory(TopicFactory, posts=[])
