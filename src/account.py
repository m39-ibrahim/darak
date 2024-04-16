from flask import render_template, redirect, url_for, request, flash, session, jsonify
from flask_login import login_user, logout_user, login_required, LoginManager, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from classes.DataAccess import DatabaseController
from classes.user import User
from main import app

# Initialize Database Controller
db_controller = DatabaseController()
# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SESSION_TYPE'] = 'filesystem'

@login_manager.user_loader
def load_user(email):
    # Load user from the database based on email
    user_doc = db_controller.Select({"email": email})
    if user_doc:
        user_doc[0].pop('_id', None)  # Remove the _id field from the document
        return User(*user_doc[0])  # Assuming user_doc[0] contains the user information
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        password = request.form.get('password')
        
        # Adjust the Select method to directly use email for the query
        user_doc = db_controller.Select({"email": email})  # Ensure Select can handle a dict query
 # Remove the _id field from the document
        print("User document:", user_doc)
        print("Provided password:", password)
        if user_doc:
            user_doc[0].pop('_id', None) 
            hashed_password = user_doc[0]['password_hash']
            username = user_doc[0]['name']
            print("Hashed password from database:", hashed_password)
            if hashed_password==password:
                print("Password correct.")
                # Assuming user_doc[0] contains the user information
                user = User(*user_doc[0])  # Create a User object with the document
                login_user(user, remember=True)
                session['logged_in'] = True  # Mark user as logged in
                session['username'] = username
                print("User logged in successfully.")
                return redirect(url_for('home'))  # Redirect to the home page
            else:
                print("Incorrect password.")
                flash('Invalid email or password.')
        else:
            print("User not found.")
            flash('Invalid email or password.')
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        name = request.form.get('name')
        password = request.form.get('password')
        phone_number = request.form.get('phone_number', '')  # Default to empty string if not provided
        address = request.form.get('address', '')
        # Adjust the query to match your user document structure
        user_doc = db_controller.Select({"email": email})
        if user_doc:
            flash('Email already exists.')
            return redirect(url_for('signup'))
        # hashed_password = generate_password_hash(password)
        # Assuming you have a way to convert your user object to a dictionary for MongoDB
        u =User(name, email, phone_number, address, password)
        u.add_user()
        return redirect(url_for('login')) # Redirect to login after signup
    return render_template('login.html')



@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    session.pop('logged_in', None)  # Remove user session
    return redirect(url_for('home'))  # Adjust if your homepage's route is different
