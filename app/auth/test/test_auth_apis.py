import unittest
from ...test.base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    def test_list_users_unexpected(self):
        """ Example get without jwt token header """
        response = self.client.get(
            '/api/v1/auth/users'
        )
        self.assertEqual(response.status_code, 401)

    def test_list_users_normal(self):
        """ Expected test with Jwt header authentication """
        response = self.client.get(
            '/api/v1/auth/users',
            headers={'Authorization': 'JWT '+self.token}
        )
        self.assertEqual(response.status_code, 200)
        assert response.get_json()['status'] == 'success'

    def test_auth_signup_unexpected(self):
        """ Example: email 'registered email from base test' """
        response = self.client.post('/api/v1/auth/signup', json=self.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()['status'], 'fail')

    def test_auth_signup_normal(self):
        """  Send correct payload """
        self.data['email'] = 'anlex@gmail.com'
        response = self.client.post('/api/v1/auth/signup', json=self.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['status'], 'success')

    def test_auth_signup_unxpected_edgecase(self):
        """  Example incorrect payload """
        self.data['email'] = 'email name'
        response = self.client.post('/api/v1/auth/signup', json=self.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()['status'], 'fail')

    def test_auth_retrieve_user_unexpected(self):
        """ Example: user_id 'string' """
        response = self.client.get(
            '/api/v1/auth/users/string',
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['status'], 'fail')

    def test_auth_retrieve_user_expected(self):
        response = self.client.get(
            '/api/v1/auth/users/'+self.user_id,
            headers={'Authorization': 'JWT ' + self.token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'success')

    def test_login_unexpected(self):
        """ Example: Wrong credentials """
        data = self.data
        data['email'] = 'wrong emal'
        response = self.client.post('/api/v1/auth/login', json=data)
        self.assertEqual(response.status_code, 404)

    def test_login_normal(self):
        response = self.client.post('/api/v1/auth/login', json=self.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
