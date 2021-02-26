from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField


class AddPetForm(FlaskForm):
  """Add a pet form"""
  name = StringField("Pet Name")
  species = StringField("Species")
  photo_url = StringField("Photo URL")
  age = IntegerField("Age")
  notes = StringField("Notes")
