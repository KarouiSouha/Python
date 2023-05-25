from flask import Flask , render_template, session, redirect,request 
import random

app=Flask (__name__)
app.secret_key="guess the number"
@app.route('/')
def rand():
    if "num" not in session :
        session['num']=random.randint(1,3)
    return render_template("index.html")

@app.route('/guess',methods=["POST"])
def play():
    session["guess"]=int(request.form["guess"])
    return redirect('/')

@app.route('/replay')
def reset():
    session.clear()
    return redirect('/')
if __name__ =="__main__":
    app.run(debug=True)