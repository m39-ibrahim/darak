from main import app
from flask import render_template, request, redirect
from classes.DataAccess import DatabaseController


@app.route("/home")
@app.route("/index")
@app.route("/")
# Modify the home route function
def home():
    db_controller = DatabaseController()
    small_header_data = db_controller.db.small_header.find_one()
    header_data = db_controller.db.header.find_one()
    hero_data = db_controller.db.hero.find_one()
    sections_data = db_controller.db.section.find({}, {"name": 1, "categories": 1, "_id": 0})

    return render_template("index.html", header=header_data, hero=hero_data, small_header=small_header_data,
                           sections=sections_data)


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route('/electronic_devices.html')
def electronic_devices():
    # Handle logic for Electronic Devices page
    return render_template('electronic_devices.html')

@app.route('/home_appliances.html')
def home_appliances():
    # Handle logic for Home Appliances page
    return render_template('home_appliances.html')

@app.route('/fabrics.html')
def fabrics():
    # Handle logic for Fabrics page
    return render_template('fabrics.html')

@app.route("/categories")
def categories():
    # Logic to retrieve categories from the database
    db_controller = DatabaseController()
    categories_data = db_controller.db.categories.find({})
    return render_template("categories.html", categories=categories_data)