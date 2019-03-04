from flask import current_app
from flask_login import UserMixin
from traxiapp import db, login_manager
from datetime import datetime

class Availability(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    driver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    unavailable_from = db.Column(db.DateTime)
    unavailable_to = db.Column(db.DateTime)

class Review(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer)
    review_text = db.Column(db.String(300))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    #driver specific attributes
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    about = db.Column(db.String(300))

    # Role relationship
    roles = db.relationship('Role', secondary='userroles',backref=db.backref('users', lazy='dynamic'))

    #Review relationship
    reviewer = db.relationship('Review', foreign_keys=[Review.user_id],backref=db.backref('reviewer', lazy='joined'))
    reviewed = db.relationship('Review', foreign_keys=[Review.driver_id], backref=db.backref('reviewed', lazy='joined'))

    # Availability relationship
    availabilities = db.relationship('Availability', foreign_keys=[Availability.driver_id], backref=db.backref('driver', lazy=True))

    # profile pic
    profile_pic_filename = db.Column(db.String, default=None, nullable=True)
    profile_pic_url = db.Column(db.String, default=None, nullable=True)

    def has_roles(self):
        return self.roles

    def has_role(self, role):
        for x in self.roles:
            if x.name == role:
                return True
            else:
                continue
    
    def create_review(self, driver, rating, review_text):
        new_review = Review(reviewed=driver, reviewer=self, rating=rating, review_text=review_text)
        db.session.add(new_review)

    def get_reviews(self):
        reviews=self.reviewed
        return reviews

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


userroles = db.Table('userroles',
db.Column('user_id', db.Integer(),db.ForeignKey('user.id')),
db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


