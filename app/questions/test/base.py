# APIs Testing

# Author: P8ul Kinuthia
# https://github.com/p8ul

import unittest
from ... import create_app
app = create_app("config.TestConfig")


""" Base Test case class, initialize variables and settings """


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
