from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from classes.DataAccess import DatabaseController
from classes.user import User
from main import app

# Initialize Database Controller
db_controller = DatabaseController()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Adjust the query to match your user document structure
        user_doc = db_controller.Select({"email": email})[0]  # Assuming Select returns a list
        if user_doc and check_password_hash(user_doc['password'], password):
            user_obj = User(user_doc['_id'], user_doc['name'], user_doc['email'], user_doc['phone_number'], user_doc['address'])
            login_user(user_obj, remember=True)
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password.')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        phone_number = request.form.get('phone_number', '')  # Default to empty string if not provided
        address = request.form.get('address', '')
        # Adjust the query to match your user document structure
        user_doc = db_controller.Select({"email": email})
        if user_doc:
            flash('Email already exists.')
            return redirect(url_for('account.signup'))
        hashed_password = generate_password_hash(password, method='sha256')
        # Assuming you have a way to convert your user object to a dictionary for MongoDB
        new_user = {"name": name, "email": email, "password": hashed_password, "phone_number": phone_number,"address": address}
        db_controller.Insert(new_user)
        return redirect(url_for('account.login')) # Redirect to login after signup
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))  # Adjust if your homepage's route is different
