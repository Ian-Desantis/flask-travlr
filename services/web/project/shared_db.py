# Only instanciate db here
# import db only as needed later
# prevents circular imports
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()