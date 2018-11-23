import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'traxi1234%^'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Development Config
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/traxi'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_PASSWORD_SALT = 'fhasdgihwntlgy8f'
    SECURITY_LOGIN_USER_TEMPLATE='login.html'


# Rijswijk server
class RijswijkConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql:///traxi'
