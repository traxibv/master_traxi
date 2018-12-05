from flask import Blueprint, render_template, current_app
from traxiapp.models import User, Role

main = Blueprint('main', __name__)


@main.route('/')
#def index():
#    return render_template('index.html', title="Index")

@main.route('/home')
def home():
    drivers = User.query.join(User.roles).filter(Role.name=='driver').all()
    return render_template('home.html', title="Home", drivers=drivers)

@main.route('/about')
def about():
    return render_template('about.html', title="About")
