# endpoints for the backend "admin" side of the website
from flask import Blueprint, render_template, request, redirect, url_for, session
import json

from .db_helpers import get_trips, get_trip, search_trips
from .models import db, Trip
from .forms import AddTripForm, EditTripForm, DeleteTripForm, SearchTripForm



# admin BP, Register with app in factory
admin = Blueprint("admin", __name__)

# Put all routes here With obvious names
# all trips, Home for admin
@admin.route("/trips", methods=['GET', 'POST'])
def trip_list():
    if request.method == 'GET':

        trips = get_trips()
        sort_by = 'id'
        rev = False
        
        session['search_results'] = trips
        session['sort_by'] = sort_by
        session['rev_order'] = rev
        session['search_input'] = ''


        return render_template("trips.html", trips=trips, sort_by=sort_by, rev=rev)

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


# search for trip with similar name
@admin.route("/trips/search", methods=['POST'])
def better_search():

    input = request.form["search"]
    trips = search_trips(input)

    session['rev_order'] = False
    session['search_input'] = input
    session['search_results'] = trips

    return render_template("trips.html", trips=trips, input=input, rev=session['rev_order'], sort_by=session['sort_by'])


@admin.route("/trips/search/<string:sort_by>", methods=['GET'])
def sort_search(sort_by):
    session['rev_order'] = False

    session['sort_by'] = sort_by


    return render_template('trips.html', trips=session['search_results'], sort_by=sort_by, input=session['search_input'], rev=session['rev_order'])


@admin.route("/trips/rev", methods=['GET'])
def rev_search():

    rev = False if session['rev_order'] == True else True
    session['rev_order'] = rev

    return render_template('trips.html', trips=session['search_results'], sort_by=session['sort_by'], rev=rev, input=session['search_input'] )

