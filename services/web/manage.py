# This is the Main Run file
# CLi is the flask CLI 
from flask.cli import FlaskGroup
from project import create_app

# create_app is added to the CLI
cli = FlaskGroup(create_app=create_app)

# Here is the DB setup
@cli.command("create_db")
def create_db():
    from project.shared_db import db
    # change as needed for setting up app DB
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("load_db")
def load_db():
    from project.shared_db import db
    from project.models import Trip
    from test_data import data
    for row in data:
        trip = Trip(**row)
        db.session.add(trip)
        db.session.commit()

# fires up app
if __name__ == "__main__":
    cli()