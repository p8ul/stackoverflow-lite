from flask_script import Manager
from app import create_app
from app.migrations.db import db
import pytest
from dotenv import load_dotenv

load_dotenv()

app = create_app("config.BaseConfig")
manager = Manager(app)


@manager.command
def test():
    db.migrate_test_db()
    pytest.main(['-v', '--cov-report', 'term-missing', '--cov=app'])
    db.drop_test_database()


if __name__ == "__main__":
    manager.run()
