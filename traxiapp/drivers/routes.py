from flask import Blueprint, url_for, redirect, render_template, current_app, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from traxiapp import db, bcrypt
from traxiapp.models import User, Role


drivers = Blueprint('drivers', __name__)

@drivers.route("/drivers/<username>")
def user(username):
    user=User.query.filter_by(username=username).first()
    return render_template('user.html', user=user, title=user.username)