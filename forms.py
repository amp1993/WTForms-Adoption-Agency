 
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField,URLField, IntegerField,BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class PetAdoptionForm(FlaskForm):
        
    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species',choices=[('dog','dog'),('cat','cat'),('porcupine','porcupine')], validators=[InputRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30),Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])

class EditPetForm(FlaskForm):
    
    photo_url = URLField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available=BooleanField("Available?")