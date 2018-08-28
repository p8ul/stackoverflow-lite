import unittest
from .base import BaseTestCase


class QuestionApiTestCase(BaseTestCase):

    def test_list_questions_unexpected(self):
        """ Example: Without JWT  token header """
        response = self.client.get(
            '/api/v1/questions/'
        )
        assert response.status_code == 200
        assert response.get_json().get('status') == 'success'

    def test_list_questions_normal(self):
        """ Example: with JWT authorization header """
        response = self.client.get(
            '/api/v1/questions/',
            headers={'Authorization': 'JWT ' + self.token}
        )
        assert response.status_code == 200
        assert response.get_json()['status'] == 'success'

    def test_retrieve_question_unexpected_boundary(self):
        """ Example: question id 'non-numeric' """
        response = self.client.get(
            '/api/v1/questions/1str',
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['status'], 'fail')

    def test_retrieve_question_normal(self):
        """ Example: question_id '1' """
        response = self.client.get(
            '/api/v1/questions/1',
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'success')

    def test_retrieve_question_unexpected_edgecase(self):
        """ Example: question_id [] """
        response = self.client.get(
            '/api/v1/questions/[]',
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['status'], 'fail')

    def test_post_question_unexpected(self):
        """ Example: Send unexpected paylaod """
        data = {
            'title': [],
            'body': {}
        }

        response = self.client.post(
            '/api/v1/questions/', json=data,
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()['status'], 'fail')

    def test_post_question_normal(self):
        """ Example: Send Expected paylaod """
        data = {
            'title': 'Test title',
            'body': 'Test body',
            'user': self.user_id
        }

        response = self.client.post(
            '/api/v1/questions/', json=data,
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['status'], 'success')

    def test_update_question_unexpected_boundary(self):
        """ Example: Send unexpected paylaod """
        data = {
            'user': self.user_id
        }

        response = self.client.put(
            '/api/v1/questions/1909090k', json=data,
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()['status'], 'fail')

    def test_delete_question_unexpected(self):
        """ Example: undefined question_id """
        response = self.client.delete(
            '/api/v1/questions/None',
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()['status'], 'fail')

    def test_delete_question_normal(self):
        """ Example: Send Expected payload """
        self.test_post_question_normal()
        response = self.client.delete(
            '/api/v1/questions/'+str(self.data.get('question_id')),
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()['status'], 'fail')


if __name__ == '__main__':
    unittest.main()
