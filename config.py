import os


# default config
class BaseConfig(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DATABASE_URI = "postgresql://stack:stack@127.0.0.1:5432/stack"
    TEST_DATABASE_URI = "postgresql://test_db:stack@127.0.0.1:5432/stack"
    TEST_DB = 'test_db'
    DEBUG = True
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = True