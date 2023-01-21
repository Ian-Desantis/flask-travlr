from flask.cli import FlaskGroup

from project import create_app
from project.shared_db import db


cli = FlaskGroup(create_app=create_app)


@cli.command("create_db")
def create_db():
    from project.shared_db import db
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()