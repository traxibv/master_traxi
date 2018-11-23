from flask import Blueprint, render_template, current_app
from datetime import date

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    go_live = date(2019, 6, 6)
    today = date.today()
    untill_golive = go_live-today
    return render_template('home.html', title="Home", go_live=go_live, untill_golive=untill_golive)


@main.route('/about')
def about():
    return render_template('about.html', title="About")


@main.route('/register')
def register():
    return render_template('register.html', title="Regiser")
