# All Routes for the customers and Front end

from flask import Blueprint, render_template

web = Blueprint("web", __name__) # used to register routes


# Create routes or endpoints below, naming should be self explainitory 
@web.route("/index") 
@web.route("/") 
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
    return render_template("travel.html")