
import unittest
from .base import BaseTestCase
from app.migrations.db import Database
from app.migrations.initial1 import create_tables_commands


class DatabaseTestCase(BaseTestCase):

    def test_database_configuration(self):
        db = Database()
        self.assertEqual(len(db.config.keys()), 4)

    def test_database_tables(self):
        self.assertEqual(len(create_tables_commands), 6)


if __name__ == '__main__':
    unittest.main()
