from flask import Flask, render_template, request, redirect

from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def all_users():
    return render_template("all_users.html", users=User.read_all())

@app.route('/users/new')
def new_user():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    User.create(request.form)
    return redirect('/users')


if __name__=="__main__":
    app.run(debug=True)




