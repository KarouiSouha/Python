from flask import Flask,render_template,request,redirect
from users import USER
app = Flask(__name__)

@app.route('/users')
def show_users():
    USER.show_users()
    return render_template("all_users.html",u=USER.show_users())

@app.route('/process',methods=['POST'])
def create_users():
    USER.creat(request.form)
    print('++++++++',request.form)
    return redirect('/users')
@app.route('/users/new')
def rend():
    return render_template("add_a_new_user.html")



if __name__ == '__main__':
    app.run(debug=True)