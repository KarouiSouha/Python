from flask_app import app
from flask import Flask, render_template,session, request, redirect
from flask_app.models.user import USER
from flask_app.models.recipe import RECIPE
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

# ? ========== LOGIN PAGE ==========
@app.route("/")
def show_form():

    return render_template("register.html")

# * ========== REGISTER method --- ACTION


@app.route("/users/register", methods=["post"])
def user_register():

    if not USER.validate(request.form):
        return redirect("/")

    # hash the password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': pw_hash
    }
    # Save the user in DB
    user_id = USER.create_user(data)
    # store the user_id in session
    session["user_id"] = user_id
    return redirect("/recipes")
# * =============== LOGIN =============


@app.route("/users/login", methods=["POST"])
def login():

    # TODO Validate the user's email and password (Both are required !)

    data = {
        "email": request.form["email"]
    }

    user_in_db = USER.get_by_email(data)
    # if email not found
    if not user_in_db:
        flash("invalid credentials", "log")
        return redirect("/")

    # check password hash
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid credentials", "log")
        return redirect("/")

    # All Good up to here
    session['user_id'] = user_in_db.id
    return redirect("/recipes")

# ---------- dashboard- view
# ? ========== Dashboard PAGE ==========


@app.route("/recipes")
def dash():

#! route guard
    if 'user_id' not in session:
     return redirect("/")

    data = {
      "id":  session["user_id"]
    }
    logged_user = USER.get_by_id(data)
    rep=RECIPE.get_all()
    print(rep)
    return render_template("recipes.html", user=logged_user, rep=rep)

# ------------ LOGOUT --------------


@app.route("/logout")
def logout():
# clear the session
 session.clear()
 return redirect("/")