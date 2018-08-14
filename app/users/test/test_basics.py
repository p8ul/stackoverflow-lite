### APIs Testing

# Author: P8ul Kinuthia
# https://github.com/p8ul
import unittest
from .base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    """ Test List users api """
    def test_list_userss(self):
        response = self.client.get('/api/v1/users/')
        assert response.status_code == 200
        assert response.get_json()['status'] == 'success'

    """ Test retrieve users api """
    def test_retrieve_user(self):
        response = self.client.get('/api/v1/users/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'success')

    """ Test retrieve user api """
    def test_post_update(self):
        """ Initialize test data """
        data = {
            'username': 'P8ul',
            'email': 'pkinuthia10@gmail.com',
            'password': 'sdfsdfsdf'
        }

        """ Post request"""
        response = self.client.post('/api/v1/users/', json=data)

        """ Test status """
        self.assertEqual(response.status_code, 201)

        """ Test if a user is created """
        self.assertEqual(response.get_json()['status'], 'success')
        self.assertEqual(response.get_json()['data']['username'], data.get('username'))
        self.assertEqual(response.get_json()['data']['email'], data.get('email'))

        user_id = str(response.get_json()['data']['id'])

        """ PUT request"""
        # update data
        data['username'] = 'New Name'
        data['email'] = 'p8ul@github.com'

        response = self.client.put('/api/v1/users/'+user_id+'/', json=data)
        """ Test if a question is updated """
        self.assertEqual(response.get_json()['status'], 'success')
        self.assertEqual(response.get_json()['data']['username'], data.get('username'))
        self.assertEqual(response.get_json()['data']['email'], data.get('email'))


if __name__ == '__main__':
    unittest.main()
