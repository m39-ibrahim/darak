from main import app
from flask import render_template
from classes.DataAccess import DatabaseController

# Function to fetch necessary data
def fetch_data():
    db_controller = DatabaseController()
    small_header_data = db_controller.db.small_header.find_one()
    header_data = db_controller.db.header.find_one()
    hero_data = db_controller.db.hero.find_one()
    sections_data = db_controller.db.section.find({}, {"name": 1, "categories": 1, "_id": 0})
    return small_header_data, header_data, hero_data, sections_data

# Home route
@app.route("/home")
@app.route("/index")
@app.route("/")
def home():
    small_header_data, header_data, hero_data, sections_data = fetch_data()
    return render_template("index.html", header=header_data, hero=hero_data, small_header=small_header_data, sections=sections_data)

# About us route
@app.route("/about_us")
def about_us():
    small_header_data, header_data, hero_data, sections_data = fetch_data()
    return render_template("about_us.html", header=header_data, hero=hero_data, small_header=small_header_data, sections=sections_data)

# Electronic devices route
@app.route('/electronic_devices.html')
def electronic_devices():
    small_header_data, header_data, hero_data, sections_data = fetch_data()
    return render_template('electronic_devices.html', header=header_data, hero=hero_data, small_header=small_header_data, sections=sections_data)

# Home appliances route
@app.route('/home_appliances.html')
def home_appliances():
    small_header_data, header_data, hero_data, sections_data = fetch_data()
    return render_template('home_appliances.html', header=header_data, hero=hero_data, small_header=small_header_data, sections=sections_data)

# Fabrics route
@app.route('/fabrics.html')
def fabrics():
    small_header_data, header_data, hero_data, sections_data = fetch_data()
    return render_template('fabrics.html', header=header_data, hero=hero_data, small_header=small_header_data, sections=sections_data)

# Categories route
@app.route("/categories")
def categories():
    db_controller = DatabaseController()
    categories_data = db_controller.db.categories.find({})
    small_header_data, header_data, hero_data, sections_data = fetch_data()
    return render_template("categories.html", categories=categories_data,  header=header_data, hero=hero_data, small_header=small_header_data, sections=sections_data)
