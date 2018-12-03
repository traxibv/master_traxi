from flask import current_app
from flask_login import UserMixin
from traxiapp import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    roles = db.relationship('Role', secondary='userroles',backref=db.backref('users', lazy='dynamic'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


userroles = db.Table('userroles',
db.Column('user_id', db.Integer(),db.ForeignKey('user.id',)),
db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)