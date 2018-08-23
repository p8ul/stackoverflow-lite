import unittest
from .. import create_app
from config import BaseConfig


app = create_app("config.TestConfig")


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.data = {
            'username': 'Paul',
            'email': 'pkinuthia10@gmail.com',
            'password': 'password',
            'database': BaseConfig.TEST_DB
        }
        """ Login to get a JWT token """
        self.client.post('/api/v1/auth/signup', json=self.data)
        response = self.client.post('/api/v1/auth/login', json=self.data)
        self.token = response.get_json().get('auth_token')
        self.user_id = str(response.get_json()['id'])

    def tearDown(self):
        # method to invoke after each test.
        pass
