import unittest

from ... import create_app
app = create_app("config.TestConfig")


class BaseTestCase(unittest.TestCase):
    """A base test case."""
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        # method to invoke before each test.
        self.client = app.test_client()
        self.data = {
            'username': 'Paul',
            'email': 'pkinuthia10@gmail.com',
            'password': 'password'
        }
        """ Login to get a JWT token """
        self.client.post('/api/v1/auth/signup', json=self.data)
        response = self.client.post('/api/v1/auth/login', json=self.data)
        self.token = response.get_json().get('auth_token')
        self.user_id = str(response.get_json()['id'])

    def tearDown(self):
        # method to invoke after each test.
        pass
