import psycopg2
import psycopg2.extras

from .initial1 import migrations
from config import BaseConfig
from ..utils import db_config


class Database:
    def __init__(self, config):
        self.config = db_config(config)
        self.database = self.config.get('database')

    def test(self):
        con = psycopg2.connect(**self.config)
        con.autocommit = True

        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("select * from pg_database where datname = %(database_name)s", {'database_name': self.database})
        databases = cur.fetchall()
        if len(databases) > 0:
            print(" * Database {} exists".format(self.database))
            for command in migrations:
                try:
                    cur.execute(command)
                    con.commit()
                except Exception as e:
                    print(e)
        else:
            print(" * Database {} does not exists".format(self.database))
        con.close()


db = Database(BaseConfig.SQLALCHEMY_DATABASE_URI)
