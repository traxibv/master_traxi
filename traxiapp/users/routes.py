from flask import Blueprint, url_for, redirect, render_template, current_app, flash
from flask_login import current_user, login_user, logout_user
from traxiapp.users.forms import LoginForm, RegisterForm
from traxiapp import db
from traxiapp.models import User
from werkzeug.security import generate_password_hash, check_password_hash


users = Blueprint('users', __name__)


# url route for the registration page
@users.route('/register',  methods=['GET', 'POST'])
def register():
    # instantiate the registration form
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'{form.username.data} created an account!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Registration', form=form)


# url route for the login page
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not check_password_hash(user.password, form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('users.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.home'))      
    return render_template('login.html', title='Sign in', form=form)


# url route for the logout page
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))