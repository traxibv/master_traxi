from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from traxiapp.models import User
from flask_login import current_user

class ReviewForm(FlaskForm):
    rating = RadioField('Rating', choices=[('1','horrible'),('2','awefull'),('3','doable'),('4','good'),('4','excellent')])
    review_text = TextAreaField('Care to expand on that sir?', validators=[DataRequired(), Length(max=300)])
    submit = SubmitField('Submit Review')
