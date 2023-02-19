""""
Auth.py

This contains all of the routes for authenticating a user.
"""

from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user

from ...shared_db import db
from ..users.models import User
from .forms import LoginForm, AddUser

auth_bp = Blueprint('auth_bp', __name__)

# signs up a user
@auth_bp.route('/signup', methods=['GET','POST'])
def signup():
    form = AddUser(request.form)
    # gets form data
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()  # if this returns a user, the email already exists in database
        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists', category='error')
            return render_template('admin/auth/signup.html', form=form)
        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = User(email, name, generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        flash('User Created: %s' % name)
        return redirect(url_for('users_bp.profile', name=name))
    # flash('Please Check Required Fields', category='error')
    return render_template('admin/auth/signup.html', form=form)
    
# login a user
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth_bp.login', form=form))  # if user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('users_bp.profile'))
    
    return render_template('admin/auth/login.html', form=form)

# logout a user
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin_bp.home'))