"""
auth/admin.py

admin homepage
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_bp = Blueprint('admin_bp', __name__)

# homepage for admins
@admin_bp.route('/admin')
def home():
    return render_template('admin/admin_home.html')