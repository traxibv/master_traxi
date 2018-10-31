from traxiapp import db
from traxiapp import login_manager
from flask import current_app
from flask_login import UserMixin
from hashlib import md5


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80))

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Driver(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50)nullable=False)
    location = db.Column(db.String(80)nullable=Flase)
    user_id = db.Column(bd.Integer, db.ForeignKey('user.id'))
                                                  ))
    description=db.Column(db.Text(300))
    fun_fact=db.Column(db.Text(300))
    no_bookings=db.Column(db.Numeric(10, 0))
    rating=db.Column(db.Numeric(10, 2))
