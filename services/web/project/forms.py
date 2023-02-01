# These are Forms from the front end
# Add any new forms needed here and import them individually later

from wtforms import StringField, validators, SubmitField, DecimalField, IntegerField
from flask_wtf import FlaskForm

# use obvious naming for each form
class AddTripForm(FlaskForm):
    name = StringField('Trip Name', [validators.Length(min=3, max=25)])
    length = IntegerField('Length of Stay', [validators.Length(min=1, max=3)])
    start = StringField('Start Date', [validators.Length(min=6, max=35)])
    resort = StringField('Resort Name', [validators.Length(min=6, max=35)])
    perPerson = DecimalField('Per Person Rate', [validators.Length(min=6, max=35)])
    image = StringField('Img file (name)', [validators.Length(min=6, max=35)])
    description = StringField('Description (HTML)', [validators.Length(min=6, max=256)])
    submit = SubmitField('Add Trip')

class EditTripForm(FlaskForm):
    name = StringField('Trip Name', [validators.Length(min=3, max=25)])
    length = IntegerField('Length of Stay', [validators.Length(min=4, max=35)])
    start = StringField('Start Date', [validators.Length(min=6, max=35)])
    resort = StringField('Resort Name', [validators.Length(min=6, max=35)])
    perPerson = DecimalField('Per Person Rate', [validators.Length(min=6, max=35)])
    image = StringField('Img file (name)', [validators.Length(min=6, max=35)])
    description = StringField('Description (HTML)', [validators.Length(min=6, max=256)])
    submit = SubmitField('Edit Trip')

class DeleteTripForm(FlaskForm):
    name = StringField('Trip Name', [validators.Length(min=3, max=25)])
    submit = SubmitField('Delete Trip')

class SearchTripForm(FlaskForm):
    search_input = StringField('Search Trip ID', [validators.Length(min=3, max=25)])
    submit = SubmitField('Search Trip')