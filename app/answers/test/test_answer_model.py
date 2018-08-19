# APIs Testing

# Author: P8ul
# https://github.com/p8ul

import unittest
from ...test.base import BaseTestCase
from ..models import Table

table = Table()


class FlaskTestCase(BaseTestCase):

    """ Test question model  """
    def test_question_model(self):
        query = table.query()
        self.assertIsInstance(query, type([]))

    def test_model_filter(self):
        query = table.filter_by()
        self.assertEqual(query, [])

    def test_model_save(self):
        query = table.save()
        self.assertEqual(query, None)

    def test_model_update(self):
        query = table.update()
        self.assertEqual(query, 404)

    def test_model_delete(self):
        query = table.delete()
        self.assertEqual(query, None)

    def test_model_question_author(self):
        query = table.question_author()
        self.assertEqual(query, False)

    def test_model_answer_author(self):
        query = table.answer_author()
        self.assertEqual(query, False)

    def test_model_accept(self):
        query = table.update_accept_field()
        self.assertEqual(query, True)

    def test_model_update_answer(self):
        query = table.update_answer()
        self.assertEqual(query, True)

    def test_model_init(self):
        keys = table.config.keys()
        self.assertIn(list(keys)[0], ['password', 'user', 'database', 'host'])
        self.assertEqual(len(list(keys)), 4)


if __name__ == '__main__':
    unittest.main()
