# Application factory for initializing app
# Put only top level application configuation logic here
# uses blueprints to bring in any other modules created
from flask import Flask, render_template

from .models import *

# Application Factory
def create_app():

    # set up app configs
    app = Flask(__name__)
    app.config.from_object('project.config.Config')
        
    # register Blueprints of other modules
    from .routes import web
    app.register_blueprint(web)
    from .trip_routes import admin
    app.register_blueprint(admin)

    # set top level routes
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    db.init_app(app) # sets db to app 

    with app.app_context():
        return app