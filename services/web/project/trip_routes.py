from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Trip
from .forms import AddTripForm, EditTripForm, DeleteTripForm


# routes for the db admin stuff 
admin = Blueprint("admin", __name__)

# db Helpers
def get_trips():
    try:
        trips = db.session.execute(db.select(Trip).order_by(Trip.name)).scalars()
    except:
        trips = None
    return trips

def get_trip(id):
    try:
        trip = db.session.execute(db.select(Trip).filter_by(id=id)).scalar_one()
    except:
        trip = None
    return trip

@admin.route("/trips")
def trip_list():
    trips = get_trips()
    return render_template("trips.html", trips=trips)

@admin.route("/trips/<int:id>")
def trip_details(id):
    trip = db.get_or_404(Trip, id)
    return render_template("trips/details.html", trip=trip)


# add trip routes
@admin.route("/trips/add", methods=["GET", "POST"])
def add_trip():
    print("entered add_trip")
    form = AddTripForm(request.form)
    if request.method == 'POST':
        print("POST")
        # if form.validate():
        print('Skipping form validation for now')
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
        print("Commited, redirecting now", trip.id)
        return redirect(url_for("admin.trip_details", id=trip.id))
    print("huh? what went wrong?")
    return render_template("trips/add.html", form=form)

@admin.route("/trips/edit/<int:id>", methods=["GET", "POST"])
def edit_trip(id):
    print('entered edit trip')
    trip = get_trip(id)
    form = EditTripForm(request.form)

    if request.method == 'POST':
        print("POST")
        print("Skipping validation for now")
        trip.name=request.form["name"],
        trip.length=request.form["length"],
        trip.start=request.form["start"],
        trip.resort=request.form["resort"],
        trip.perPerson=request.form["perPerson"],
        trip.image=request.form["image"],
        trip.description=request.form["description"],

        db.session.commit()
        print('commited')
        return redirect(url_for("admin.trip_details", id=trip.id))

    print('exiting')
    return render_template("trips/edit.html", form=form, trip=trip)

@admin.route("/trips/<int:id>/delete", methods=["GET", "POST"])
def delete_trip(id):
    trip = db.get_or_404(Trip, id)
    form = DeleteTripForm(request.form)
    
    if request.method == 'POST':
        confirm = True if request.form['name'] == trip.name else False
        if confirm:
            db.session.delete(trip)
            db.session.commit()
            return redirect(url_for("admin.trip_list"))

        return render_template("trips/delete.html", form=form, trip=trip)


    return render_template("trips/delete.html", form=form, trip=trip)