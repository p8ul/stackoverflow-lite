import unittest
from random import randint
from .base import BaseTestCase


class AuthApiTestCase(BaseTestCase):

    def test_list_users_without_jwt_header(self):
        """ Example get without jwt token header """
        response = self.client.get(
            '/api/v1/auth/users'
        )
        self.assertEqual(response.status_code, 401)

    def test_list_users_with_jwt_header(self):
        """ Expected test with Jwt header authentication """
        response = self.client.get(
            '/api/v1/auth/users',
            headers={'Authorization': 'JWT '+self.token}
        )
        self.assertEqual(response.status_code, 200)

    def test_auth_signup_already_signed_up_user(self):
        """ Example: email 'registered email from base test' """
        response = self.client.post('/api/v1/auth/signup', json=self.data)

        self.assertEqual(response.status_code, 404)

    def test_auth_signup_unregistered_user(self):
        """  Send correct payload """
        self.data['email'] = 'pk' + str(randint(0, 9)) + '@gmail.com'
        response = self.client.post('/api/v1/auth/signup', json=self.data)
        self.data['test_logout_token'] = response.get_json().get('auth_token')
        self.assertEqual(response.status_code, 201)

    def test_auth_user_logout(self):
        """ Test logout endpoint"""
        response = self.client.post('/api/v1/auth/login', json=self.data)
        token = response.get_json().get('auth_token')
        response = self.client.post(
            '/api/v1/auth/logout',
            headers={'Authorization': 'JWT ' + token}
        )
        self.assertEqual(response.status_code, 200)

    def test_auth_signup_invalid_email(self):
        """  Example incorrect payload """
        self.data['email'] = 'email name'
        response = self.client.post('/api/v1/auth/signup', json=self.data)

        self.assertEqual(response.status_code, 404)

    def test_auth_retrieve_user_invalid_user_id_parameter(self):
        """ Example: user_id 'string' """
        response = self.client.get(
            '/api/v1/auth/users/string',
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json().get('error'), 'The resource does not exist')

    def test_auth_retrieve_user_valid_user_id_parameter(self):
        response = self.client.get(
            '/api/v1/auth/users',
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 200)

    def test_login_invaid_email(self):
        """ Example: Wrong credentials """
        data = self.data
        data['email'] = 'wrong emal'
        response = self.client.post('/api/v1/auth/login', json=data)
        self.assertEqual(response.status_code, 404)

    def test_login_correct_credentials(self):
        response = self.client.post('/api/v1/auth/login', json=self.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
