from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)
app.secret_key="guess the number."
@app.route('/')
def index():
    if "counter" not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template("index.html")


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route("/counter", methods=["POST"])
def view_count():
    if request.form["alt"]=="add":
        session["counter"] += 1
    elif request.form["alt"]=="reset":
        session["counter"] = 0

    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)