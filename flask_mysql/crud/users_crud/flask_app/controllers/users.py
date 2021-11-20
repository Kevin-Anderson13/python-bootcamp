from flask import  render_template, request, redirect

from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

# Read All
@app.route('/users')
def all_users():
    return render_template("all_users.html", users=User.read_all())

@app.route('/users/new')
def new_user():
    return render_template("new_user.html")

# Create Post
@app.route('/user/create',methods=['POST'])
def create():
    User.create(request.form)
    return redirect('/users')

# Update Get
@app.route('/user/<int:id>/update')
def update(id):
    data ={
        "id":id
    }
    return render_template("edit_user.html",user=User.read_one(data))

# Read One
@app.route('/user/<int:id>/show_one')
def show(id):
    data ={
        "id":id
    }
    return render_template("one_user.html",user=User.read_one(data))

# Update Post
@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

# Delete or Destroy
@app.route('/user/<int:id>/delete')
def delete(id):
    data ={
        'id':id
    }
    User.delete(data)
    return redirect('/users')