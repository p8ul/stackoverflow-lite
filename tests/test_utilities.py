
import unittest
from .base import BaseTestCase
from app.auth.blacklist import Blacklist
from app.utils import (
    encode_auth_token,
    db_config,
    valid_email,
    is_blacklisted
)


class UtilitiesTestCase(BaseTestCase):

    def test_token_blacklisting(self):
        token = "token"
        response = Blacklist({'token': token}).blacklist_token()
        self.assertIsNotNone(response)

    def test_if_token_is_blacklisted(self):
        token = "token"
        Blacklist({'token': token}).blacklist_token()
        response = is_blacklisted(token)
        self.assertIsNotNone(response)

    def test_utils_encode_auth_token(self):
        payload = encode_auth_token(self.user_id)
        self.assertEqual(len(str(payload).split('.')), 3)

    def test_utils_base_config(self):
        config = db_config()
        self.assertEqual(len(config.keys()), 4)

    def test_utils_valid_email_unexpected(self):
        valid = valid_email('invalid-email')
        self.assertEqual(valid, None)

    def test_utils_valid_email_normal(self):
        valid = valid_email('pkinuthia10@gmail.com')
        self.assertIsNotNone(valid)


if __name__ == '__main__':
    unittest.main()
