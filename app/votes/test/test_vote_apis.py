# APIs Testing

# Author: P8ul
# https://github.com/p8ul

import unittest
from ...test.base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    """ Test List votes api """
    def test_votes_api(self):
        response = self.client.post(
            '/api/v1/questions/answers/vote/1', data=self.data,
            headers={'Authorization': 'JWT ' + self.token}
        )
        assert response.status_code == 400


if __name__ == '__main__':
    unittest.main()
