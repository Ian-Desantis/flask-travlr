# Flask Application Factory
# register all routes here as shown below

from flask import Flask, render_template

# Application Factory
def create_app():
    app = Flask(__name__)

    # Top level routes
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    # register routes to application (Blueprints)
    from .web_routes import web
    app.register_blueprint(web)

    with app.app_context():
        return app