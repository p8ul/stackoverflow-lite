import unittest
import pytest

from ... import create_app
app = create_app("config.TestConfig")


# @pytest.fixture
class BaseTestCase(unittest.TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        # method to invoke before each test.
        self.client = app.test_client()

    def tearDown(self):
        # method to invoke after each test.
        pass
