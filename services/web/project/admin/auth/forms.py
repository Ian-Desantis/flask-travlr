# forms.py

from wtforms import StringField, SubmitField, PasswordField, validators
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.Length(min=6, max=50), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
    ])
    submit = SubmitField('Login')

