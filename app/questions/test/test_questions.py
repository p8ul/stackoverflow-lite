import unittest
from .base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    def test_list_questions(self):
        """ Test List questions api """
        response = self.client.get('/api/v1/questions/')
        assert response.status_code == 200
        assert response.get_json()['status'] == 'success'

    def test_retrieve_question(self):
        """ Test retrieve questions api """
        response = self.client.get('/api/v1/questions/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'success')

    def test_post_question(self):
        """ Test post request """
        response = self.client.post('/api/v1/questions/', json=self.data)
        self.assertEqual(response.status_code, 201)
        print(response.get_json())

if __name__ == '__main__':
    unittest.main()
