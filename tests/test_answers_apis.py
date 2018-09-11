import unittest
from .base import BaseTestCase


class AnswersApiTestCase(BaseTestCase):

    def test_list_answers_unexpected(self):
        """ Without JWT authorization header """
        response = self.client.get(
            '/api/v1/questions/answers'
        )
        self.assertEqual(response.status_code, 200)

    def test_list_answers_normal(self):
        """ With JWT authorization"""
        response = self.client.get(
            '/api/v1/questions/answers',
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 200)

    def test_post_update(self):
        data = {
            'title': 'Test title',
            'body': 'Test body',
            'answer_body': 'Test answer',
            'user': self.user_id
        }

        """ Add test question"""
        self.client.post(
            '/api/v1/questions/', json=data,
            headers={'Authorization': 'JWT ' + self.token}
        )

        response = self.client.get(
            '/api/v1/questions/',
            headers={'Authorization': 'JWT ' + self.token}
        )
        question_id = response.get_json().get('results')[0].get('question_id')

        """ Test post answer """
        response = self.client.post(
            '/api/v1/questions/'+str(question_id)+'/answers', json=data,
            headers={'Authorization': 'JWT ' + self.token}
        )

        """ Test status """
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
