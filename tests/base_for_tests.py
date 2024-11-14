from flask_testing import TestCase

from config import create_app
from db import db


def mock_uuid():
    return "1234-5678"


class TestBaseForApp(TestCase):
    def create_app(self):
        return create_app("config.TestingConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
