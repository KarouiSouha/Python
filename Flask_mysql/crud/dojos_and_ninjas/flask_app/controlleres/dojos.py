from flask_app import app
from flask import render_template,session,request,redirect
from flask_app.models.dojo import DOJO
@app.route('/create_dojo',methods=['POST'])
def add_dojo():
    DOJO.create_dojo(request.form)
    return redirect('/dojo')

@app.route('/dojo')
def index():
    dojos=DOJO.show_dojos()
    return render_template("index.html",all_dojo=dojos)
@app.route("/dojo/<int:dojo_id>")
def show_dojo(dojo_id):
    data={
        'id':dojo_id
    }
    show=DOJO.show_ninja_in_dojo(data)
    return render_template('show_dojo.html',show=show)