import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('TRAXI_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Development server
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql:///traxi'
    UPLOADED_PROFILEPICTURES_DEST = basedir + '/traxiapp/static/profile_pics/'
    UPLOADED_PROFILEPICTURES_URL = 'http://traxiworld.com/static/profile_pics/'
