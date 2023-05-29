from flask import Flask, render_template, request, redirect
from user import USER
app = Flask(__name__)
@app.route('/users')
def show_users():
    users = USER.show_users()
    print(users)
    return render_template("all_user.html",users=users)

@ app.route('/process',methods=['POST'])
def create_users():
    USER.create_user(request.form)
    return redirect('/users')
@app.route('/users/new')
def rend():
    return render_template("add_new_user.html")


@app.route('/user/edit/<int:id>')
def edit(id):
    user=USER.get_one(id)
    return render_template("edit_user.html",user=user)

@app.route('/user/show/<int:id>')
def show(id):
    
    user=USER.get_one(id)
    return render_template("show_user.html", user=user)


@app.route('/user/edit',methods=['POST'])
def update():
    USER.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    USER.destroy(data)
    return redirect('/users')

@app.route('/')
def redir():
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)