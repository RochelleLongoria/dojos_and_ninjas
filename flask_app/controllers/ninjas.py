from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojos
from flask_app import app

from flask_app.models.ninja import Ninjas
# ---------Initial Page-------

# Route New Ninja Page.


@app.route('/ninja/new')
def ninja():
    Dojos.Get_dojos()
    return render_template('ninja.html', dojos=Dojos.Get_dojos())

# Process New Ninja Info from form
# Redirect to Dojo Show after Creating a new ninja


@app.route('/ninja/process', methods=['POST'])
def process():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojos_id']
    }
    Ninjas.save(data)
    return redirect(f'/dojo_show/{request.form["dojos_id"]}')

# Display all Ninjas who were added to dojo
