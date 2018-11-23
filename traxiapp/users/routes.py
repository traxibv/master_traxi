
from flask import Blueprint, url_for, redirect, render_template, current_app, request, flash
from traxiapp.users.forms import LoginForm, RegisterForm
from traxiapp import db
from traxiapp.models import User, Role
from flask_security import login_user, logout_user, current_user, SQLAlchemyUserDatastore
from flask_security.utils import hash_password, verify_password, login_user, logout_user

users = Blueprint('users', __name__)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = hash_password(form.password.data)
        if form.driver_checkbox.data is True:
            user_datastore.create_user(username=form.username.data, email=form.email.data, password=hashed_password, roles=['driver'])
        else:
            user_datastore.create_user(username=form.username.data, email=form.email.data, password=hashed_password,roles=['end-user'])
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Registration', form=form)



@users.route('/login_user', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        user = user_datastore.get_user(form.email.data)
        login_user(user)
        redirect(url_for('main.home'))
        return redirect(url_for('main.home'))
    return render_template('login.html', title='Sign in', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
