# endpoints for the backend "admin" side of the website
from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Trip
from .forms import AddTripForm, EditTripForm, DeleteTripForm, SearchTripForm


# admin BP, Register with app in factory
admin = Blueprint("admin", __name__)

# Helper functions
def get_trips():
    try:
        # gets all trips
        return db.session.execute(db.select(Trip).order_by(Trip.name)).scalars()
        
    except:
        # if problem
        return  None

# gets one trip, by id
def get_trip(id):
    try:
        return db.session.execute(db.select(Trip).filter_by(id=id)).scalar_one()
    except:
        return  None

def search_trips_by_name(name):
    try:
        trips = db.session.execute(db.select(Trip).filter(Trip.name.ilike(f'%{name}%'))).scalars().fetchall()
        return trips
    except:
        return  None

# Put all routes here With obvious names

# all trips, Home for admin
@admin.route("/trips")
def trip_list():
    trips = get_trips()
    return render_template("trips.html", trips=trips)

# gets trip by ID
@admin.route("/trips/<int:id>")
def trip_details(id):
    trip = db.get_or_404(Trip, id)
    return render_template("trips/details.html", trip=trip)

@admin.route("/trips/add", methods=["GET", "POST"])
def add_trip():
    form = AddTripForm(request.form)
    if request.method == 'POST':
        trip = Trip(
            name=request.form["name"],
            length=request.form["length"],
            start=request.form["start"],
            resort=request.form["resort"],
            perPerson=request.form["perPerson"],
            image=request.form["image"],
            description=request.form["description"],
        )
        db.session.add(trip)
        db.session.commit()
        return redirect(url_for("admin.trip_details", id=trip.id))
    return render_template("trips/add.html", form=form)

# Edit trip by id
@admin.route("/trips/edit/<int:id>", methods=["GET", "POST"])
def edit_trip(id):
    trip = get_trip(id)
    form = EditTripForm(request.form)
    # sets new values
    if request.method == 'POST':
        trip.name=request.form["name"],
        trip.length=request.form["length"],
        trip.start=request.form["start"],
        trip.resort=request.form["resort"],
        trip.perPerson=request.form["perPerson"],
        trip.image=request.form["image"],
        trip.description=request.form["description"],

        db.session.commit()
        return redirect(url_for("admin.trip_details", id=trip.id))

    return render_template("trips/edit.html", form=form, trip=trip)

# Deletes Trip By Id
@admin.route("/trips/<int:id>/delete", methods=["GET", "POST"])
def delete_trip(id):
    trip = db.get_or_404(Trip, id)
    form = DeleteTripForm(request.form)
    
    if request.method == 'POST':
        # confirms you want to delete trip
        # forces you to enter trip name exacatly before delete
        confirm = True if request.form['name'] == trip.name else False
        if confirm:
            db.session.delete(trip)
            db.session.commit()
            return redirect(url_for("admin.trip_list"))

        return render_template("trips/delete.html", form=form, trip=trip)


    return render_template("trips/delete.html", form=form, trip=trip)

# searches for trip by similar name
@admin.route("/trips/search", methods=['POST'])
def search_details():

    input = request.form["search"]
    trips = search_trips_by_name(input)
    
    return render_template("trips.html", trips=trips)
