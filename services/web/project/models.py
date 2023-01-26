# DB models for SQLalchemy
# use these for creating tables and query objects
# FLASK-SQLalchemy ORM

from .shared_db import db

# DB models created here
class Trip(db.Model):
    __tablename__ = 'trips' # override model name for table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    length = db.Column(db.String, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    resort = db.Column(db.String, nullable=False)
    perPerson = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    
    # init not required
    # use this to force required fields during init
    def __init__(self, name, length, start, resort,
    perPerson, image, description) -> None:
        super().__init__()
        self.name = name
        self.length = length
        self.start = start
        self.resort = resort
        self.perPerson = perPerson
        self.image = image
        self.description = description