from ...test.base import BaseTestCase
from ..validatons import validate_user_details


class FlaskTestCase(BaseTestCase):

    def test_auth_user_validation(self):
        """ Validate user details """
        data = {"email": "", 'password': ''}
        user = validate_user_details(data)
        assert user.get('email') == 'Invalid email. Please enter a valid email'

