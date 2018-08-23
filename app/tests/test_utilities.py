
import unittest
from app.tests.base import BaseTestCase
from ..utils import (
    encode_auth_token,
    db_config,
    valid_email
)


class UtilitiesTestCase(BaseTestCase):

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
