from flask import Flask, render_template
from .models import *

def create_app():

    app = Flask(__name__)
    app.config.from_object('project.config.Config')
        
    # register Blueprints 
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

    db.init_app(app)

    with app.app_context():
        return app