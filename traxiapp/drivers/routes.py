from flask import Blueprint, render_template, current_app
from traxiapp.drivers.forms import RegisterDriverForm

drivers = Blueprint('drivers', __name__ )

@drivers.route('/register_driver')
def register_driver():
    form = RegisterDriverForm()
    # if form.validate_on_submit():
    #     hashed_password = generate_password_hash(form.password.data, method='sha256')
    #     new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return '<h1> New user has been created </h1>'
    return render_template('register_driver.html', title='Register driver', form=form)