# APIs Testing

# Author: P8ul Kinuthia
# https://github.com/p8ul

import unittest
from .base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    """ Test List answers api """
    def test_list_answers(self):
        response = self.client.get(
            '/api/v1/questions/answers',
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'success')

    """ Test answers CRUD api """
    def test_post_update(self):
        """ Initialize test data """
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

        """ Test if a question is created """
        self.assertEqual(response.get_json()['status'], 'success')


if __name__ == '__main__':
    unittest.main()
