### APIs Testing

# Author: P8ul Kinuthia
# https://github.com/p8ul

import unittest
from .base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    """ Test List questions api """
    def test_list_questions(self):
        response = self.client.get('/api/v1/questions/')
        assert response.status_code == 200
        assert response.get_json()['status'] == 'success'

    """ Test retrieve questions api """
    def test_retrieve_question(self):
        response = self.client.get('/api/v1/questions/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'success')

    """ Test retrieve questions api """
    def test_post_update(self):
        """ Initialize test data """
        data = {
            'title': 'Test title',
            'body': 'Test body',
            'user': 'p8ul'
        }

        """ Post request"""
        response = self.client.post('/api/v1/questions/', json=data)

        """ Test status """
        self.assertEqual(response.status_code, 201)

        """ Test if a question is created """
        self.assertEqual(response.get_json()['status'], 'success')
        self.assertEqual(response.get_json()['data']['title'], data.get('title'))
        self.assertEqual(response.get_json()['data']['body'], data.get('body'))

        question_id = str(response.get_json()['data']['id'])

        """ Post answers """
        answer = {
            'user': 'Paul Kinuthia',
            'answer': 'Correct Answer Test'
        }
        response = self.client.post('/api/v1/questions/'+question_id+'/answer', json=answer)
        self.assertEqual(response.get_json()['status'], 'success')
        self.assertEqual(response.get_json()['data'].get('answer'), answer.get('answer'))

        """ PUT request"""
        # update data
        data['name'] = 'New Title'
        data['body'] = 'Updated body'

        response = self.client.put('/api/v1/questions/'+question_id+'/', json=data)
        """ Test if a question is updated """
        self.assertEqual(response.get_json()['status'], 'success')
        self.assertEqual(response.get_json()['data']['title'], data.get('title'))
        self.assertEqual(response.get_json()['data']['body'], data.get('body'))


if __name__ == '__main__':
    unittest.main()
