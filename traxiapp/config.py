import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG=False
    SECRET_KEY=os.environ.get('TRAXI_DB_PASS')
    SQLALCHEMY_TRACK_MODIFICATIONS=False


# Development Config
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost/traxi'


# Rijswijk server
class RijswijkConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql:///traxi'

