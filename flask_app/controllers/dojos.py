from flask import render_template, redirect, request,session
from flask_app.models.dojo import Dojos
from flask_app import app
from flask_app.models.ninja import Ninjas

# ---------Initial Page-------
# ------Make links redirect the 'Dojo Show' Page.
#Home Link
@app.route('/')
@app.route('/dojo/signup')
def home():
    dojo = Dojos.Get_dojos()
    return render_template('dojo.html', dojos = dojo)

# Render DojoShow Page
@app.route('/dojo_show/<int:id>')
def Show(id):
    data ={"id": id}
    return render_template('dojo_show.html', dojo = Dojos.get_one(data), ninjas = Dojos.show_ninjas(data))

# Process New Dojo Form
@app.route('/process/dojo', methods = ['POST'])
def save():
    data = {
        "name" : request.form ['name']
    }
    Dojos.save(data)
    return redirect('/dojo/signup')

# Dojo Show
#Should I put <dojo.name> so that it pulls the dojo name and not ninja name?
@app.route('/dojos/<int:id>')
def dojo_roster(id):
    data = {
        "id": id
    }
    return redirect('/dojo_show', dojos = Dojos.dojo_roster(data))