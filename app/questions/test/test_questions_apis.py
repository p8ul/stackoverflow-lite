# APIs Testing

# Author: P8ul
# https://github.com/p8ul

import unittest
from ...test.base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    """ Test List questions api """
    def test_list_questions(self):
        response = self.client.get(
            '/api/v1/questions/',
            headers={'Authorization': 'JWT ' + self.token}
        )
        assert response.status_code == 200
        assert response.get_json()['status'] == 'success'

    """ Test retrieve questions api """
    def test_retrieve_question(self):
        response = self.client.get(
            '/api/v1/questions/1',
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'success')

    """ Test retrieve questions api """
    def test_post_update(self):
        """ Initialize test data """
        data = {
            'title': 'Test title',
            'body': 'Test body',
            'user': self.user_id
        }

        """ Post request"""
        response = self.client.post(
            '/api/v1/questions/', json=data,
            headers={'Authorization': 'JWT ' + self.token}
        )

        """ Test status """
        self.assertEqual(response.status_code, 201)

        """ Test if a question is created """
        self.assertEqual(response.get_json()['status'], 'success')


if __name__ == '__main__':
    unittest.main()
