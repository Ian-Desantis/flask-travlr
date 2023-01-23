# this is the main run file. 
# python manage.py run -h 0.0.0.0

from flask.cli import FlaskGroup

from project import create_app


cli = FlaskGroup(create_app=create_app) 


if __name__ == "__main__":
    cli()