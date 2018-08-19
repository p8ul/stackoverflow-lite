from .base import BaseTestCase
from ..validatons import validate_user_details


class FlaskTestCase(BaseTestCase):

    """ Test user details validation """
    def test_model_crud(self):
        data = {"email": "", 'password': ''}
        # Test Create
        instance = validate_user_details(data)
        assert instance.get('email') == 'Invalid email. Please enter a valid email'

