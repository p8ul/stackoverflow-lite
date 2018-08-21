import os


# default config
class BaseConfig(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    # DATABASE_URI = "postgres://tvhuxucdtigrin:fc7e1f53efe5f81b6a6d3dacad8f79605cd0973d0ae5efa5ac29b3976b48f938@ec2-54-83-13-119.compute-1.amazonaws.com:5432/d393cevo034f77"
    DATABASE_URI = "postgresql://stack:stack@127.0.0.1:5432/stack"
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