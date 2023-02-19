"""
users/user_routes.py

Routes for the user's endpoints
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user

users_bp = Blueprint('users_bp', __name__, template_folder='templates')

# Brings them to their welcome page.
@users_bp.route('/profile')
@login_required
def profile():
    return render_template('admin/users/profile.html', name=current_user.name)