from flask import Blueprint, render_template
from .trip_routes import get_trips

# routes for the website 
web = Blueprint("web", __name__)

@web.route("/") 
def index():
    return render_template("index.html")

@web.route("/index",) 
def index_literal():
    return render_template("index.html")

@web.route("/home") 
def home():
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
    trips = get_trips()
    return render_template("travel.html", trips=trips)



