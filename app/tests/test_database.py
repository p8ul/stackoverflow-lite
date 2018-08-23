
import unittest
from config import BaseConfig
from .base import BaseTestCase
from ..migrations.db import Database
from ..migrations.initial1 import create_tables_commands


class DatabaseTestCase(BaseTestCase):

    def test_database_configuration(self):
        db = Database(BaseConfig.DATABASE_URI)
        self.assertIn(db.config.get('database'), [BaseConfig.TEST_DB, 'stack', 'test_db'])

    def test_database_tables(self):
        self.assertEqual(len(create_tables_commands), 5)


if __name__ == '__main__':
    unittest.main()
