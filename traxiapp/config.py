import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG=False
    SECRET_KEY=os.environ.get('TRAXI_DB_PASS')
    SQLALCHEMY_TRACK_MODIFICATIONS=False


# Development server
class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql:///traxi'

