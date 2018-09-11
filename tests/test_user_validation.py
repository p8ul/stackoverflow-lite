from .base import BaseTestCase
from app.auth.validatons import validate_user_details


class TestUserTestCase(BaseTestCase):

    def test_auth_user_validation(self):
        """ Validate user details """
        data = {"email": "", 'password': ''}
        user = validate_user_details(data)
        assert user.get('email') == 'Invalid email. Please enter a valid email'

