from main import app
from flask import render_template
from classes.DataAccess import DatabaseController
from flask import request, jsonify

db_controller = DatabaseController()
# Function to fetch necessary data
def fetch_data():
    small_header = db_controller.db.small_header.find_one()
    header_data = db_controller.db.header.find_one()
    hero_data = db_controller.db.hero.find_one()
    sections_data = db_controller.db.section.find({}, {"name": 1, "categories": 1, "_id": 0})
    return small_header, header_data, hero_data, sections_data

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


# # Categories route
# @app.route("/categories", methods=["GET", "POST"])
# def categories():
#     if request.method == "POST":
#         # Extract the selected category from the JSON data
#         selected_category = request.json.get("category")
#         # Perform actions with the selected category (e.g., store it in the database, process it, etc.)
#         # For now, let's just print it
#         print("Selected category:", selected_category)
#         # Return a JSON response indicating success (you can customize this as needed)
#         return jsonify({"message": "Category received successfully."}), 200
#     categories_data = db_controller.db.categories.find({})
#     small_header_data, header_data, hero_data, sections_data = fetch_data()

#     return render_template("categories.html", categories=categories_data, header=header_data, hero=hero_data, small_header=small_header_data, sections=sections_data,)
