import unittest
from .base import BaseTestCase


class AnswersTestCase(BaseTestCase):
    def test_answer_post_unexpected_input(self):
        """ Wrong payload Example: '{}' """
        answer = ''
        response = self.client.post('/api/v1/questions/' + self.question_id + '/answer', json=answer)
        self.assertEqual(response.get_json()['status'], 'error')
        self.assertEqual(response.get_json().get('message'), 'Bad request')

    def test_post_answer_normal(self):
        """ Post correct answers payload """
        answer = {
            'answer': 'Correct Answer Test'
        }
        response = self.client.post('/api/v1/questions/' + self.question_id + '/answer', json=answer)
        self.assertEqual(response.get_json()['status'], 'success')
        self.assertEqual(response.get_json().get('data').get('answer'), answer.get('answer'))
