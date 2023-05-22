from flask import Flask, render_template, session, redirect,request
import random
app = Flask(__name__)

@app.route('/')
def index():
     if "num" not in session:
        session['num'] =random.randint(1, 100) 
     return render_template("index.html")
if("__name__"=="__main__"):
    app.run(debug=True)
