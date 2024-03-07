from main import app
from flask import render_template, request, redirect
from classes.DataAccess import DatabaseController


@app.route("/home")
@app.route("/index")
@app.route("/")
def home():
    db_controller = DatabaseController()  # Initialize the database controller
    # Ensure you're accessing the correct collection here
    small_header_data = db_controller.db.small_header.find_one()
    header_data = db_controller.db.header.find_one()
    hero_data = db_controller.db.hero.find_one()
    
    return render_template("index.html", header=header_data, hero=hero_data, small_header=small_header_data)

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")
