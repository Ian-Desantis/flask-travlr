from .shared_db import db
from .models import Trip
from json import dumps
from dataclasses import dataclass


@dataclass
class NewTrip():
    id: int
    name: str
    length: int
    start: str
    resort: str
    perPerson: float
    image: str
    description: str

def convert_trip(trip):
    new_trip = NewTrip(trip.id, trip.name, trip.length,
    trip.start.strftime('%Y-%m-%d'), trip.resort, float(trip.perPerson),
    trip.image, trip.description)
    return new_trip

def convert_trips(trips):
    new_trips = [convert_trip(trip) for trip in trips]
    return new_trips


# Helper functions
def get_trips(sort='name'):
    try:
        # gets all trips
        result = db.session.execute(
            db.select(Trip)
            .order_by(getattr(Trip,sort))
            ).scalars()
        trips = convert_trips(result)
        return trips 
    except:
        return None  
        
    

# gets one trip, by id
def get_trip(id):
    try:
        results = db.session.execute(
            db.select(Trip)
            .filter_by(id=id)
            ).scalar_one()
        return convert_trips(results)
    except:
        return  None

def search_trips_by_name(trip_name, sort="name"):
    try:
        trips = db.session.execute(
            db.select(Trip)
            .filter(
                Trip.name.ilike(f'%{trip_name}%'))
                .order_by(getattr(Trip,sort))
                ).scalars()

        return convert_trips(trips)
    except Exception as e: 
        print(e)


def search_trips(search_input, sort="name"):
    try:
        trips = db.session.execute(
            db.select(Trip)
            .filter(
                Trip.name.ilike(f'%{search_input}%') |
                Trip.resort.ilike(f'%{search_input}%') |
                Trip.description.ilike(f'%{search_input}%')
                )
                .order_by(getattr(Trip,sort))
                ).scalars()
        return convert_trips(trips)

    except Exception as e: 
        print(e)