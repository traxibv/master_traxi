from flask import Blueprint, url_for, redirect, render_template, current_app, request
from flask_login import current_user, login_user, logout_user, login_required
from traxiapp.users.forms import LoginForm, RegisterUserForm
from traxiapp import db
from traxiapp.models import User
from werkzeug.security import generate_password_hash, check_password_hash


users = Blueprint('users', __name__)

# url route for the login page
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not check_password_hash(user.password, form.password.data):
            flash('Invald username or passowrd')
            return redirect(url_for('users.login')) 
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netlog != '':
            next_page=url_for('main.home')
        return redirect(next_page)      
    return render_template('login.html', title='Sign in', form=form)

# url route for the logout page
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


# url route for the registration page
@users.route('/register_user',  methods=['GET', 'POST'])
def register_user():
    # instantiate the registration form
    form = RegisterUserForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New user has been created </h1>'
    return render_template('register_user.html', title='Registration User', form=form)

#url for register page
@users.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)