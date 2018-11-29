from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from traxiapp.config import DevelopmentConfig


migrate = Migrate()
bootstrap = Bootstrap()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # initialize extensions
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'users.login'
    login_manager.login_message_category = 'info'

    # security

    # import blueprints
    from traxiapp.users.routes import users
    from traxiapp.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(main)


    return app


