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
    from traxiapp.drivers.routes import drivers
    from traxiapp.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(drivers)
    app.register_blueprint(main)

    from traxiapp.models import Role, User
    @app.before_first_request
    def before_first_request():
        with app.app_context():
            db.create_all()
            # create roles if they do not exist at service restart
            if not Role.query.filter_by(name='driver').first():
                driver_role = Role(name='driver')
                db.session.add(driver_role)
                db.session.commit()
            if not Role.query.filter_by(name='end-user').first():
                end_user_role = Role(name='end-user')
                db.session.add(end_user_role)
                db.session.commit()
            # create drivers if they do not exist at service restart
            if not User.query.filter_by(username='testdriver1').first():
                pw_testdriver1 = bcrypt.generate_password_hash('testdriver1').decode('utf-8')
                testdriver1 = User(username='testdriver1', email='testdriver1@test.com', password=pw_testdriver1, country='Uganda', city='Kampala', about='Fawaka. I am the absolute best driver you will ever meet. My subaru looks like a Bentley and you will be treated like a King !!!' )
                db.session.add(testdriver1)
                testdriver1_role = Role.query.filter_by(name='driver').first()
                testdriver1.roles.append(testdriver1_role)
                db.session.commit()
            if not User.query.filter_by(username='testdriver2').first():
                pw_testdriver2 = bcrypt.generate_password_hash('testdriver2').decode('utf-8')
                testdriver2 = User(username='testdriver2', email='testdriver2@test.com', password=pw_testdriver2, country='Uganda', city='Entebe', about='Bonjour. I am the absolute 2nd best driver you will ever meet. My Bentley looks like a Subaru and you will be treated like an animal !!!' )
                db.session.add(testdriver2)
                testdriver2_role = Role.query.filter_by(name='driver').first()
                testdriver2.roles.append(testdriver2_role)
                db.session.commit()
            # create end-users if they do not exist at service restart
            if not User.query.filter_by(username='testuser1').first():
                pw_testuser1 = bcrypt.generate_password_hash('testuser1').decode('utf-8')
                test_user1 = User(username='testuser1', email='testuser1@test.com', password=pw_testuser1)
                db.session.add(test_user1)
                testuser1_role = Role.query.filter_by(name='end-user').first()
                test_user1.roles.append(testuser1_role)
                db.session.commit()
            if not User.query.filter_by(username='testuser2').first():
                pw_testuser2 = bcrypt.generate_password_hash('testuser2').decode('utf-8')
                test_user2 = User(username='testuser2', email='testuser2@test.com', password=pw_testuser2)
                db.session.add(test_user2)
                testuser2_role = Role.query.filter_by(name='end-user').first()
                test_user2.roles.append(testuser2_role)
                db.session.commit()
    return app


