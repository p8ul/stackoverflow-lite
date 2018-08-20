from flask_bcrypt import Bcrypt
from ..utils import valid_email

b_crypt = Bcrypt()


def validate_user_details(data):
    errors = {}
    if not valid_email(data.get('email')):
        errors['email'] = 'Invalid email. Please enter a valid email'
    if not data.get('email'):
        errors['password'] = 'Password required'
    if data.get('user'):
        errors['user_exist'] = 'User already exists. Please Log in.'
    return errors


def validate_login(data):
    errors = {}
    return errors
