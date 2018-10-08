from flask import Blueprint, url_for, redirect, render_template, current_app
from traxiapp.users.forms import LoginForm, RegisterForm
from traxiapp import db
from traxiapp.models import User
from werkzeug.security import generate_password_hash, check_password_hash


users = Blueprint('users', __name__)

# url route for the login page

@users.route('/login', methods=['GET', 'POST'])
def login():
    # instantiate the login form
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                return redirect(url_for('main.home'))       
        return '<h1> Invalid password or username </h1>'
    return render_template('login.html', title='Sign in', form=form)


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
        return '<h1> New user has been created </h1>'
    return render_template('register.html', title='Registration', form=form)