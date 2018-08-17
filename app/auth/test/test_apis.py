# APIs Testing

# Author: P8ul
# https://github.com/p8ul
import unittest
from .base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    """ Test List users api """
    def test_list_users(self):
        response = self.client.get(
            '/api/v1/auth/users',
            headers={'Authorization': 'JWT '+self.token}
        )
        self.assertEqual(response.status_code, 200)
        assert response.get_json()['status'] == 'success'

    """ Test retrieve user api """
    def test_post_update(self):
        """ Post request"""
        # self.client.delete('/api/v1/auth/delete', json=self.data)
        response = self.client.post('/api/v1/auth/signup', json=self.data)
        """ Test status """
        self.assertEqual(response.status_code, 202)

        """ Test if a user is created """
        self.assertEqual(response.get_json()['status'], 'fail')

    """ Test retrieve users api """
    def test_retrieve_user(self):
        response = self.client.get(
            '/api/v1/auth/users/'+self.user_id,
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'success')

    def test_login(self):
        response = self.client.post('/api/v1/auth/login', json=self.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
