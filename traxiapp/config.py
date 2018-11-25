import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG=False
    SECRET_KEY = os.environ.get('TRAXI_KEY') or 'super secret'
    SQLALCHEMY_TRACK_MODIFICATIONS=False


# Development server
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost/traxi'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_PASSWORD_SALT = 'fhasdgihwntlgy8f'

