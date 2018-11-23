from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me ?')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired('Username is required'), Length(min=4, max=15, message='Username must be between 4 and 15')])
    email = StringField('Email', validators=[InputRequired('Email is required'), Email(
        message='Email is invalid')])
    password = PasswordField(
        'Password', validators=[InputRequired(), Length(min=8, max=20, message='Password must be between 8 and 20')])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     InputRequired('Email confirmation is required'), EqualTo('password')])
    driver_checkbox = BooleanField('Register as driver?')
    submit = SubmitField('Submit registration')
