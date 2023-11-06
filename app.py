from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, Pet
from forms import PetAdoptionForm, EditPetForm


app = Flask(__name__)
app.debug = True

# Configure the Flask Debug Toolbar
app.config['SECRET_KEY'] = 'mysecretkey'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_agency"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



with app.app_context():
    
    connect_db(app)
    db.create_all()
    
    

@app.route('/')
def homepage():
    # Make Homepage Listing Pets
    
    pets = Pet.query.all()
    
    return render_template('homepage.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = PetAdoptionForm()
    
    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data,
        )

        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_add_form.html', form=form)
    

@app.route('/pets/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    
     # Display edit form and commit changes. 
     
    pet=Pet.query.get_or_404(pet_id)
    form=EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url=form.photo_url.data,
        pet.notes=form.notes.data
        pet.available=form.available.data
        db.session.commit()
        flash(f'Updated details for {pet.name}.')
        return redirect ('/')
    
    else:
        return render_template('pet_edit_form.html', pet=pet, form=form)
    

   
@app.route('/pets/<int:pet_id>/delete', methods=['POST'])
def delete_pet(pet_id):
    
    pet = Pet.query.get_or_404(pet_id)
    if pet:
        db.session.delete(pet)
        db.session.commit()
        return redirect('/')
        flash (f'Pet has been deleted')

    
if __name__ == '__main__':
    app.run()
