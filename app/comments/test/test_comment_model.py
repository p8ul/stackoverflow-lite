# APIs Testing

# Author: P8ul
# https://github.com/p8ul

import unittest
from ...test.base import BaseTestCase
from ..models import Table

table = Table()


class FlaskTestCase(BaseTestCase):

    """ Test votes model  """
    def test_model_save(self):
        query = table.save()
        self.assertEqual(query, False)

    def test_model_init(self):
        keys = table.config.keys()
        self.assertIn(list(keys)[0], ['password', 'user', 'database', 'host'])
        self.assertEqual(len(list(keys)), 4)


if __name__ == '__main__':
    unittest.main()
