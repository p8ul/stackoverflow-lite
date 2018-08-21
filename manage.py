from flask_script import Manager
from app import create_app
from app.migrations.db import db
import pytest
import os

app = create_app("config.BaseConfig")
manager = Manager(app)


@manager.command
def test():
    os.environ['APP_SETTINGS'] = 'TESTING'
    db.migrate_test_db()
    pytest.main(['-v', '--cov=app', 'app/questions/test/test_questions_apis.py'])
    db.drop_test_database()


if __name__ == "__main__":
    manager.run()
