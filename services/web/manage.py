# this is the main run file. 
# keep this thin as possible
# usage: python manage.py run -h 0.0.0.0

from flask.cli import FlaskGroup

from project import create_app

# Where the application is created upon construction
cli = FlaskGroup(create_app=create_app) 

if __name__ == "__main__":
    cli()