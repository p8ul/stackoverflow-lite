from flask_script import Manager
from app import create_app
from app.migrations.db import db
import pytest
import py.test
import os

app = create_app("config.BaseConfig")
manager = Manager(app)


@manager.command
def test():
    os.environ['APP_SETTINGS'] = 'TESTING'
    db.migrate_test_db()
    py.test(['-v', '--cov-report', 'term-missing', '--cov=app', 'app/tests'])
    os.environ['APP_SETTINGS'] = 'PRODUCTION'
    db.drop_test_database()


if __name__ == "__main__":
    manager.run()
