from flask import Blueprint, url_for, redirect, render_template, current_app, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from traxiapp import db, bcrypt
from traxiapp.models import User, Role, Review
from traxiapp.drivers.forms import ReviewForm


drivers = Blueprint('drivers', __name__)

@drivers.route("/<username>/profile", methods=['GET', 'POST'])
def user(username):
    user=User.query.filter_by(username=username).first()
    reviews=Review.query.filter_by(driver_id=user.id).all()
    return render_template('profile.html', user=user, title=user.username, reviews=reviews)

@drivers.route("/drivers/<username>/create_review",  methods=['GET', 'POST'])
def create_review(username):
    form = ReviewForm()
    driver=User.query.filter_by(username=username).first()
    user=User.query.filter_by(username=current_user.username).first()
    if form.validate_on_submit():
        current_user.create_review(driver, form.rating.data, form.review_text.data)
        db.session.commit()
        reviews=Review.query.filter_by(driver_id=driver.id).all()
        return render_template('user.html',user=driver, reviews=reviews)
    return render_template('create_review.html', user=driver, form=form, title=driver.username)
    
    