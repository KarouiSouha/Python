from flask_app import app
from flask import render_template,session,request,redirect
from flask_app.models.dojos import DOJO
from flask_app.models.ninjas import NINJA
@app.route('/ninjas')
def ninja():
    all_dojos=DOJO.show_dojos()
    return render_template("new_ninja.html",all_dojos=all_dojos)
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