from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$')
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class User:
    db_name = 'login_reg'

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # create user
    @classmethod
    def create_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        user_from_db = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(user_from_db[0])

    # Validate new user
    @staticmethod
    def validate_registration(form_data):
        is_valid = True
        if len(form_data['first_name']) < 2:
            is_valid = False
            flash("User's First name must be at least 2 characters!!!!!!")
        if len(form_data['last_name']) < 2:
            is_valid = False
            flash("User's Last name must be at least 2 characters!!!!!!")
        if not EMAIL_REGEX.match(form_data['email']):
            is_valid = False
            flash("This is not a valid email!!!!!")
        if form_data['password'] != form_data['confirm_password']:
            is_valid = False
            flash("Passwords must match")
        if len(form_data['password']) < 10:
            is_valid = False
            flash("Password must be 10 or more characters!!!!!")
        return is_valid

    # Validate logging in
    @staticmethod
    def validate_login(form_data, data_dictionary):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        list_of_users = connectToMySQL(User.db_name).query_db(query, data_dictionary)
        if len(list_of_users) < 1: # This is just if nobody is found
            is_valid = False
            flash("Invalid login")
            return is_valid
        # Check Password below
        current_user = list_of_users[0]
        user_instance = User(current_user) # Creates an instance of a User
        if not bcrypt.check_password_hash(user_instance.password, form_data['password']):
            is_valid = False
            # if this is False after checking password
            flash("Invalid login")
        # If the credentials are correct, return id.
        if is_valid:
            is_valid = user_instance.id
        return is_valid


