from .base import BaseTestCase
from ..models import Table


class FlaskTestCase(BaseTestCase):

    """ Test signup api """
    def test_model_crud(self):
        # Test Create
        instance = Table.save(self.data)
        assert instance == self.data

        # Test query
        isinstance(Table.query(), type([]))
