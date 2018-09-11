
import unittest
from .base import BaseTestCase
from app.comments.models import Comment

comment = Comment()


class CommentModelTestCase(BaseTestCase):

    def test_model_save_normal(self):
        query = comment.save()
        self.assertEqual(query, False)

    def test_model_init(self):
        keys = comment.config.keys()
        self.assertIn(list(keys)[0], ['password', 'user', 'database', 'host'])
        self.assertEqual(len(list(keys)), 4)


if __name__ == '__main__':
    unittest.main()
