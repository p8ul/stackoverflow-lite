import unittest
from ...test.base import BaseTestCase
from ..models import Vote

vote = Vote()


class FlaskTestCase(BaseTestCase):

    def test_model_save(self):
        query = vote.save()
        self.assertEqual(query, None)

    def test_model_delete(self):
        query = vote.delete()
        self.assertEqual(query, None)

    def test_model_vote_exist(self):
        query = vote.vote_exists()
        self.assertEqual(query, None)

    def test_model_vote_exist(self):
        query = vote.vote()
        self.assertEqual(query, False)

    def test_model_update_vote(self):
        query = vote.update_vote()
        self.assertEqual(query, False)

    def test_model_create_vote(self):
        query = vote.create_vote()
        self.assertEqual(query, False)

    def test_model_init(self):
        keys = vote.config.keys()
        self.assertIn(list(keys)[0], ['password', 'user', 'database', 'host'])
        self.assertEqual(len(list(keys)), 4)


if __name__ == '__main__':
    unittest.main()
