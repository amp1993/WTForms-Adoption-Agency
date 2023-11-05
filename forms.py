 
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField,URLField, IntegerField,BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class PetAdoptionForm(FlaskForm):
        
    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species',choices=[(1,'dog'),(2,'cat'),(3,'porcupine')], validators=[InputRequired()])
    photo_url = URLField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30),Optional()])
    notes = StringField('Notes', validators=[Optional()])
    available=BooleanField('Available')
