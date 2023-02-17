# forms.py

from wtforms import StringField, SubmitField, PasswordField, validators
from flask_wtf import FlaskForm


class AddUser(FlaskForm):
    name = StringField('Name', [validators.Length(min=2, max=25), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6, max=50), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm_pass = PasswordField('Confirm Password', [validators.DataRequired()])
    submit = SubmitField('Add User')

