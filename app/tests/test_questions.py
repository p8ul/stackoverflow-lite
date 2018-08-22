import unittest
from .base import BaseTestCase


class QuestionsTestCase(BaseTestCase):

    def test_list_questions_expected(self):
        """ Expected endpoint """
        response = self.client.get('/api/v1/questions/')
        assert response.status_code == 200
        assert response.get_json()['status'] == 'success'

    def test_retrieve_question_unexpected(self):
        """ Example: question_id 'string' should be a number """
        response = self.client.get('/api/v1/questions/s/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['status'], 'error')

    def test_retrieve_question_normal(self):
        """ Example: question_id '1'  """
        response = self.client.get('/api/v1/questions/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'success')

    def test_post_question_unexpected_input(self):
        """ Send unexpected payload """
        response = self.client.post('/api/v1/questions/', json={})
        self.assertEqual(response.status_code, 400)

    def test_post_question_normal(self):
        """ Send correct post json payload  """
        response = self.client.post('/api/v1/questions/', json=self.data)
        self.assertEqual(response.status_code, 201)
        print(response.get_json())


if __name__ == '__main__':
    unittest.main()
