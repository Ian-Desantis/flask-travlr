# This is where the "routes" or endpoints 
# for the client side of the website are

from flask import Blueprint, render_template
from .trip_routes import get_trips

# web blueprint of routes 
# to be registerd with the app in the factory 
web = Blueprint("web", __name__)

# Put routes here, Use obvious names
@web.route("/")
@web.route("/home")
@web.route("/index") 
def index():
    return render_template("index.html")

@web.route("/about") 
def about():
    return render_template("about.html")

@web.route("/contact") 
def contact():
    return render_template("contact.html")

@web.route("/meals") 
def meals():
    return render_template("meals.html")

@web.route("/news") 
def news():
    return render_template("news.html")

@web.route("/rooms") 
def rooms():
    return render_template("rooms.html")

@web.route("/travel") 
def travel():
    trips = get_trips() # populates front end from db
    return render_template("travel.html", trips=trips)