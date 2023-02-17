from .shared_db import db
from .models import Trip
from dataclasses import dataclass

# serializable version of the db model
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

# converts db model to dataclass. formats some data
def convert_trip(trip):
    new_trip = NewTrip(trip.id, 
                    trip.name, 
                    trip.length,
                    trip.start.strftime('%Y-%m-%d'), 
                    trip.resort, 
                    float(trip.perPerson),
                    trip.image, 
                    trip.description)
    return new_trip

# turns query result into json(ish) format
# can work with the data better like this without repeated queries to the db
def convert_trips(trips):
    new_trips = [convert_trip(trip) for trip in trips]
    return new_trips


# Helper functions for the db queries
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
        return convert_trip(results)
    except:
        return  None

# gets one trip, by id
def get_trip_as_trip(id):
    try:
        results = db.session.execute(
            db.select(Trip)
            .filter_by(id=id)
            ).scalar_one()
        return results
    except:
        return  None

# better search algo, looks in all text fields
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