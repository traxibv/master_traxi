from flask import Blueprint, render_template, current_app
from traxiapp import db
from traxiapp.models import User, Role
from traxiapp.main.forms import SearchForm

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
@main.route('/home', methods=['GET'])
def home():
    drivers = User.query.join(User.roles).filter(Role.name=='driver').all()
    results_cities = db.session.query(User.city).distinct()
    cities = [city for city, in results_cities]
    cities.remove(None)
    return render_template('home.html', title="Home", drivers=drivers, cities=cities)

@main.route('/about')
def about():
    return render_template('about.html', title="About")
