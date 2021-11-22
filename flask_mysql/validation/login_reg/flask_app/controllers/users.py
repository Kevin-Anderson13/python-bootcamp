from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Login and Register Page
@app.route("/")
def login_reg_page():
    return render_template("login_reg.html")


# Handle Registration
@app.route("/register", methods=["POST"])
def reg_new_user():
    if not User.validate_registration(request.form):
        return redirect("/")
    # If registration passes
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']) # hashed password
    }
    # save id of new user - NOT instance of User class in session...
    session['user_id'] = User.create_new_user(data)
    return redirect("/dashboard")


# Handle Login
@app.route("/login", methods=["POST"])
def user_login():
    data = {
        "email": request.form["email"],
    }
    user_exists = User.validate_login(request.form, data)
    if user_exists == False:
        return redirect("/")
    session['user_id'] = user_exists
    return redirect("/dashboard")

@app.route("/dashboard")
def user_dashboard():
    data = {
        "id": request.form['user_id']
    }
    current_user = User.get_one_user(data)
    return render_template("dashboard.html",user=current_user)

# Sign Out
@app.route("/logout")
def log_out():
    session.clear()
    return redirect("/")

