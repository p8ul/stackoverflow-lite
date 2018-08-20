### APIs Testing

# Author: P8ul Kinuthia
# https://github.com/p8ul

import unittest
import pytest

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
        self.data = {
            'title': 'Test title',
            'body': 'Test body',
            'user': 'p8ul'
        }
        response = self.client.post('/api/v1/questions/', json=self.data)
        self.question_id = str(response.get_json()['data'][0]['id'])

