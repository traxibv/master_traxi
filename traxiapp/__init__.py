from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from traxiapp.config import DevelopmentConfig, RijswijkConfig
from flask_security import SQLAlchemyUserDatastore, Security


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()


def create_app(config_class=DevelopmentConfig):
    """
     App factory pattern avoids circular imports, so instead of importing
     'app' directly you import its factory. If you need the current running app
     you can use 'from flask import current_app'
     :return: app
     """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    # security
    from traxiapp.models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)

    # import blueprints
    from traxiapp.users.routes import users
    from traxiapp.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(main)

    @app.before_first_request
    def before_first_request():
        # Create any database tables that don't exist yet.
        db.create_all()
        # Create the Roles "driver" and "end-user" -- unless they already exist
        user_datastore.find_or_create_role(name='driver', description='driver')
        user_datastore.find_or_create_role(name='end-user', description='klant')
        # Create test driver and end-user
        if not user_datastore.find_user(username='testdriver'):
            user_datastore.create_user(username='testdriver', email='test@driver.com', password='test123', roles=['driver'])
        # Commit any database changes
        db.session.commit()

    return app
