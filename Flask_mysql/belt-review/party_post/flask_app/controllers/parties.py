from flask_app import app
from flask import Flask, render_template,session, request, redirect
from flask_app.models.partie import PARTY

@app.route('/parties/new')
def show():
    return render_template('add_party.html')

@app.route('/add_party',methods=['POST'])
def create_party():
    PARTY.create_partie(request.form)
    print(request.form)
    return redirect('/dashboard')

