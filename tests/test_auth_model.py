from .base import BaseTestCase
from app.auth.models import User

user = User()


class AuthModelTestCase(BaseTestCase):

    def test_auth_model_save_unexpected(self):
        """ Example: Provide wrong json payload """
        instance = user.save()
        self.assertEqual(instance, None)

    def test_auth_model_save_normal(self):
        """ Example: send correct payload """
        user = User(self.data)
        instance = user.save()
        assert instance.get('email') == self.data.get('email')

    def test_auth_model_filter_by_id_unexpected_boundary(self):
        """ Example: user_id 'string' """
        user.user_id = 'string'
        self.assertEqual(user.filter_by(), None)

    def test_auth_model_filter_by_id_expected(self):
        """ Example: user_id '1' """
        user.user_id = self.user_id
        isinstance(user.filter_by(), type([]))

    def test_auth_model_filter_by_id_unexpected_edgecase(self):
        """ Example: user_id '[]' """
        user.user_id = []
        self.assertEqual(user.filter_by(), None)

    def test_auth_model_filter_by_email_unexpected_boundary(self):
        """ Example: email 'None' """
        user.email = None
        self.assertEqual(user.filter_by_email(), [])

    def test_auth_model_filter_by_email_expected(self):
        """ Example: email 'pkinuthia10@gmail.com' """
        user.email = self.data.get('email')
        self.assertEqual(user.filter_by_email()[0].get('email'), self.data.get('email'))

    def test_auth_model_filter_by_email_unexpected_edgecase(self):
        """ Example: email '[]' """
        user.email = []
        self.assertEqual(user.filter_by_email(), [])

    def test_auth_model_update_unexpected_boundary(self):
        """ Example: email 'None' """
        user.email = None
        self.assertEqual(user.update(), False)

    def test_auth_model_update_expected(self):
        """ Example: email 'pkinuthia10@gmail.com' """
        user.email = 'joshua@j.com'
        user.username = 'p8ul'
        user.user_id = self.user_id
        self.assertEqual(user.update(), True)

    def test_auth_model_update_unexpected_edgecase(self):
        """ Example: email '[]', username 'None """
        user.email = []
        user.username = None
        self.assertEqual(user.update(), False)

    def test_auth_model_query_expected(self):
        """ Query all users in users table """
        isinstance(user.query(), type([]))
