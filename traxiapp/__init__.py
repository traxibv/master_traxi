from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from traxiapp.config import DevelopmentConfig


migrate = Migrate()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # initialize extensions
    migrate.init_app(app, db)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'users.login'
    login_manager.login_message_category = 'info'

    # import blueprints
    from traxiapp.users.routes import users
    from traxiapp.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(main)

    from traxiapp.models import Role
    @app.before_first_request
    def before_first_request():
        with app.app_context():
            db.create_all()
            if not Role.query.filter_by(name='driver').first():
                driver_role = Role(name='driver')
                db.session.add(driver_role)
                db.session.commit()
            if not Role.query.filter_by(name='end-user').first():
                end_user_role = Role(name='end-user')
                db.session.add(end_user_role)
                db.session.commit()

    return app


