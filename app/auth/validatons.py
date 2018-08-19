from ..utils import valid_email


def validate_user_details(data):
    errors = {}
    if not valid_email(data.get('email')):
        errors['email'] = 'Invalid email. Please enter a valid email'
    if not data.get('email'):
        errors['password'] = 'Password required'
    return errors
