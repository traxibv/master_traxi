import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG=False
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'traxi1234%^'
    SQLALCHEMY_TRACK_MODIFICATIONS=False


# Development server
class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql:///traxi'

