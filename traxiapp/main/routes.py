from flask import Blueprint, render_template, current_app
from datetime import datetime
from flask_nav.elements import Navbar, View
from traxiapp import nav

main = Blueprint('main', __name__)

nav.register_element('menu', Navbar(
    View('Home', 'main.home'),
    View('Login', 'users.login'),
    View('Register', 'users.register'),
    View('About', 'main.about')
))

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html', title="Home")

@main.route('/about')
def about():
    return render_template('about.html', title="About")
