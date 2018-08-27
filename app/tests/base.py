import unittest
from .. import create_app
from ..utils import decode_auth_token
from config import BaseConfig


app = create_app("config.BaseConfig")


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
        self.user_id = '1'  # str(decode_auth_token(self.token))

    def tearDown(self):
        # method to invoke after each test.
        pass
