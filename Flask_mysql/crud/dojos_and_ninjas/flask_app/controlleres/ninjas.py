from flask_app import app
from flask import render_template,session,request,redirect
from flask_app.models.dojo import DOJO
from flask_app.models.ninja import NINJA
@app.route('/ninjas')
def ninja():
    all_dojos=DOJO.show_dojo()
    return render_template("add_ninja.html",all_dojos=all_dojos)
@app.route('/add_ninjas',methods=['POST'])
def add_new_ninja():
    session["first_name"]=request.form["first_name"]
    session["last_name"]=request.form["last_name"]
    session["age"]=request.form["age"]
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    NINJA.create_ninja(data)
    return redirect('/ninjas')