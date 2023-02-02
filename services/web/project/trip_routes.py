# File for the endpoints for the backend "admin" side of the website

# library imports
from flask import Blueprint, render_template, request, redirect, url_for, session

# package imports
from .db_helpers import get_trips, get_trip, search_trips
from .models import db, Trip
from .forms import AddTripForm, EditTripForm, DeleteTripForm


# admin BP, Register with app in factory
admin = Blueprint("admin", __name__)

# Put all routes here With obvious names
# all trips, Home for admin
@admin.route("/trips", methods=['GET', 'POST'])
def trip_list():
    if request.method == 'GET':

        trips = get_trips()
        
        sort_by = 'id'
        reverse_order = False
        
        # sets up session session / resets params
        session['search_results'] = trips
        session['sort_by'] = sort_by
        session['reverse_order'] = reverse_order
        session['search_input'] = ''

        return render_template("trips.html", trips=trips, sort_by=sort_by, reverse_order=reverse_order)

# gets trip by ID
@admin.route("/trips/<int:id>")
def trip_details(id):
    trip = db.get_or_404(Trip, id)
    return render_template("trips/details.html", trip=trip)

# add trip routes
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
        db.session.commit() # insert to db

        return redirect(url_for("admin.trip_details", id=trip.id))
    # IF GET request
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

    # IF GET Request
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
        # reconfirm (bad input)
        return render_template("trips/delete.html", form=form, trip=trip)
    # if GET request
    return render_template("trips/delete.html", form=form, trip=trip)


# search for trip with similar name
@admin.route("/trips/search", methods=['POST'])
def better_search():

    # gets users input and performs search
    input = request.form["search"]
    trips = search_trips(input)

    # reset search params
    # session['reverse_order'] = False

    # sets ssearch results and input into session for use later
    session['search_input'] = input
    session['search_results'] = trips


    return render_template("trips.html", trips=trips, input=input, 
                            reverse_order=session['reverse_order'], sort_by=session['sort_by'])

# sorts the search results by field selected "sort_by"
@admin.route("/trips/search/<string:sort_by>", methods=['GET'])
def sort_search(sort_by):

    # resets sort order
    session['reverse_order'] = False
    # set sort by
    session['sort_by'] = sort_by

    return render_template('trips.html', trips=session['search_results'], 
                            sort_by=sort_by, input=session['search_input'], reverse_order=session['reverse_order'])

# Reverses the order of the search results
@admin.route("/trips/rev", methods=['GET'])
def rev_search():

    # sets session variable for ordering
    reverse_order = False if session['reverse_order'] == True else True
    session['reverse_order'] = reverse_order

    return render_template('trips.html', trips=session['search_results'], 
                            sort_by=session['sort_by'], reverse_order=reverse_order, input=session['search_input'] )

