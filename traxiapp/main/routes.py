from flask import Blueprint, render_template, current_app
from datetime import datetime

main = Blueprint('main', __name__)


@main.route('/')
#def index():
#    return render_template('index.html', title="Index")

@main.route('/home')
def home():
    return render_template('home.html', title="Home")

@main.route('/about')
def about():
    return render_template('about.html', title="About")
