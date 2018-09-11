import unittest
from .base import BaseTestCase


class VoteApiTestCase(BaseTestCase):

    """ Test List votes api """
    def test_votes_api(self):
        response = self.client.post(
            '/api/v1/questions/answers/vote/1', data=self.data,
            headers={'Authorization': 'JWT ' + self.token}
        )
        assert response.status_code == 400


if __name__ == '__main__':
    unittest.main()
