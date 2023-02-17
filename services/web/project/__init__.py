# Application factory for initializing app
# Put only top level application configuation logic here
# uses blueprints to bring in any other modules created
from flask import Flask, render_template
from flask_login import LoginManager
from .shared_db import db
from .models import *

# Application Factory
def create_app():

    # set up app configs
    app = Flask(__name__)
    app.config.from_object('project.config.Config')

    login_manager = LoginManager()
    login_manager.login_view = 'auth_bp.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    db.init_app(app) # sets db to app 
        
    # register Blueprints of other modules
    from .routes import web
    app.register_blueprint(web)

    from .admin.admin import admin_bp
    app.register_blueprint(admin_bp)

    from .admin.auth.auth import auth_bp
    app.register_blueprint(auth_bp)

    from .admin.trips.trip_routes import trips_bp
    app.register_blueprint(trips_bp)

    from .admin.users.user_routes import users_bp
    app.register_blueprint(users_bp)

    # set top level routes
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    # The actual app being returned
    with app.app_context():
        return app