"""
users/models.py

User model for Flask Login
"""
from flask_login import UserMixin

from ...shared_db import db

# represents a user of the website
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
