from .base import BaseTestCase
from ..models import Table


class FlaskTestCase(BaseTestCase):

    """ Test signup api """
    def test_model_crud(self):
        table = Table(self.data)
        # Test Create
        instance = table.save()
        assert instance.get('email') == self.data.get('email')

        # Test query
        isinstance(table.query(), type([]))
