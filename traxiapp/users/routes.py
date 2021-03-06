import os
from pathlib import Path
import glob
from flask import Blueprint, url_for, redirect, render_template, current_app, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from traxiapp import db, bcrypt
from traxiapp.users.forms import LoginForm, RegisterForm, UpdateAccountForm
from traxiapp.models import User, Role, Availability
from traxiapp import profilepictures


users = Blueprint('users', __name__)

# Template filters
@users.app_template_filter('datetimeformat')
def datetimeformat(value, format='%d %B %Y'):
    return value.strftime(format)

# url route for the registration page
@users.route('/register',  methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    # instantiate the registration form
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        # create entry in the association (userroles) table according to the value of the checkbos
        if form.driver_checkbox.data is True:
            driver_role = Role.query.filter_by(name='driver').first()
            new_user.roles.append(driver_role)
        else:
            user_role = Role.query.filter_by(name='end-user').first()
            new_user.roles.append(user_role)
        db.session.commit()
        flash(f'{form.username.data} created an account!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


# url route for the login page
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('users.login'))
    return render_template('login.html', title='Sign in', form=form)


# url route for the logout page
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

# url route for the account page
@users.route('/<username>/account', methods=['GET', 'POST'])
@login_required
def account(username): 
    form = UpdateAccountForm()
    if request.method== 'POST' and form.validate():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.country = form.country.data
        current_user.city = form.city.data
        current_user.about = form.about.data
        # if a profile picture is uploaded
        if 'profile_pic' in request.files:
            # chekc if user allready has avatar on the filesystem and if yes, remove it 
            basedir = Path(__file__).resolve().parents[1]
            picsdir = 'static/profile_pics'
            filepath = filepath_form = os.path.join(basedir,picsdir)
            filepath_user =  glob.glob('{}/{}_*'.format(filepath,current_user.username))
            filepath_user_string = ''.join(filepath_user)
            if os.path.exists(filepath_user_string):
                os.remove(filepath_user_string)
            # save avatar to filesystem and filename + url to the database
            filename = profilepictures.save(request.files['profile_pic'], name='{}_{}'.format(current_user.username,request.files['profile_pic'].filename))
            url = profilepictures.url(filename)
            current_user.profile_pic_filename = filename
            current_user.profile_pic_url = url
        db.session.commit()
        flash('Your account has been updated', 'success')
        if current_user.has_role('driver'):
            return redirect(url_for('drivers.user', username=current_user.username))
        else:
            return redirect(url_for('main.home'))
    elif request.method== 'POST' and not form.validate():
        return render_template('account.html', title='Account', form=form)
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.country.data = current_user.country
        form.city.data = current_user.city
        form.about.data = current_user.about
        return render_template('account.html', title='Account', form=form)
    