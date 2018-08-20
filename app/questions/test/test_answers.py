import unittest
from .base import BaseTestCase


class FlaskTestCase(BaseTestCase):
    def test_post_answer(self):
        """ Post answers """
        answer = {
            'answer': 'Correct Answer Test'
        }
        response = self.client.post('/api/v1/questions/' + self.question_id + '/answer', json=answer)
        self.assertEqual(response.get_json()['status'], 'success')
        self.assertEqual(response.get_json()['data'][0].get('answers')[0].get('answer'), answer.get('answer'))
