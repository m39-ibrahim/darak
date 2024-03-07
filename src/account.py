from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
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
        
        # Adjust the Select method to directly use email for the query
        user_doc = db_controller.Select({"email": email})  # Ensure Select can handle a dict query
        
        if user_doc and check_password_hash(user_doc[0]['password_hash'], password):
            # Assuming user_doc[0] contains the user information
            user = User(user_doc[0])  # Create a User object with the document
            login_user(user, remember=True)
            return redirect(url_for('home'))  # Redirect to the home page
        else:
            flash('Invalid email or password.')
            return redirect(url_for('login'))  # Stay on the login page if error

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
        u =User(name, email, phone_number, address, hashed_password)
        u.add_user()
        return redirect(url_for('login')) # Redirect to login after signup
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))  # Adjust if your homepage's route is different
