import unittest
import pytest

from .. import create_app
app = create_app("config.TestConfig")


class BaseTestCase(unittest.TestCase):
    """A base test case."""

    def setUp(self):
        self.client = app.test_client()
        self.data = {
            'title': 'Test title',
            'body': 'Test body',
            'user': 'p8ul'
        }
        response = self.client.post('/api/v1/questions/', json=self.data)
        self.question_id = str(response.get_json()['data'][0]['id'])
