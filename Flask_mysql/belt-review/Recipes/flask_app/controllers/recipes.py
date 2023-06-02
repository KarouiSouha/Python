from flask_app import app
from flask import Flask, render_template,session, request, redirect
from flask_app.models.recipe import RECIPE
from flask_app.models.user import USER


@app.route('/recipes/new')
def show():
  if 'user_id' in session:
    return render_template('add_new_recipe.html')
  return redirect('/')

@app.route('/add_recipe',methods=['POST'])
def create_recipe():
    if "user_id" in session:
        data={** request.form,
            'id':id}
        RECIPE.create_recipe(request.form)
        print(request.form)
        return redirect('/recipes')
    return redirect('/')

@app.route('/recipes/view/<int:id>')
def show_view(id):
    if "user_id" in session:
        data={'id':id}
        vi=RECIPE.get_one(data )
        user=USER.get_by_id({"id":session['user_id']})
        return render_template("view.html", vi=vi,user=user)
    return redirect('/')

@app.route('/recipes/edit/<int:id>')
def show_edit(id):
    if "user_id" in session:
        data={'id':id}
        rec=RECIPE.get_one(data)
        return render_template("edit.html", rec=rec)
    return redirect('/')

@app.route('/edit/<int:id>',methods=['POST'])
def update(id):
    if "user_id" in session:
       data={
        **request.form,
        'id':id
        }
       RECIPE.update(data)
       return redirect('/recipes')
    return redirect('/')


@app.route('/delete/<int:id>',methods=['POST'])
def delete(id):
    if "user_id" in session:
        data={
        'id':id
        }
        RECIPE.delete(data)
        return redirect('/recipes')
    return redirect('/')