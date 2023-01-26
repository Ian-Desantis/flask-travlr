# Config object
# Keeps config stuff separte from application

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # add required config stuff here
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dd4596c00d043688fcb78a67c6d3f15d5eeed68e95d83f08484040a07af3d82c'