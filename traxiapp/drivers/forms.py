from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional


class RegisterDriverForm(FlaskForm):
    first_name = StringField('First name', validators=[
                             DataRequired(), Length(max=30)])
    last_name = StringField('Last name', validators=[
                            DataRequired(), Length(max=30)])
    email = StringField('Email', validators=[DataRequired(), Email(
        message='Invalid email'), Length(max=50)])

    country = StringField('Country', validators=[
                          DataRequired(), Length(max=50)])
    city = StringField('City', validators=[DataRequired(), Length(max=50)])
    languages = StringField('Languages', validators=[
                            DataRequired(), Length(max=50)])
    about = TextAreaField("About you", validators=[
                          Optional(), Length(max=200)])
    fun_fact = StringField('Fun fact', validators=[
                           Optional(), Length(max=200)])

    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')
