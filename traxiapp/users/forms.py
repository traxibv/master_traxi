from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=4, max=15)])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email(
        message='Invalid email'), Length(max=50)])
    submit = SubmitField('Sign Up')
