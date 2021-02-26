from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'newKey'


connect_db(app)
db.create_all()


@app.route("/")
def show_home():
  """Display homepage"""
  pets = Pet.query.all()
  return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def new_pet():
  """Show and handle add pet form"""
  form = AddPetForm()

  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    photo_url = form.photo_url.data
    age = form.age.data
    notes = form.notes.data
    new_pet = Pet(name = name, species = species, age = age, notes = notes, photo_url=photo_url)
    db.session.add(new_pet)
    db.session.commit()
    return redirect("/")
  
  else:
    return render_template("addpet.html", form=form)
