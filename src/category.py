from flask import request, jsonify, Blueprint
from main import app
from flask import render_template
from classes.DataAccess import DatabaseController
from home import fetch_data


db_controller = DatabaseController()
category_bp = Blueprint('category', __name__)
# Categories route
@category_bp.route("/categories", methods=["GET", "POST"])
def categories():
    if request.method == "POST":
        # Extract the selected category from the JSON data
        selected_category = request.json.get("category")
        # Perform actions with the selected category (e.g., store it in the database, process it, etc.)
        # For now, let's just print it
        print("Selected category:", selected_category)
        # Return a JSON response indicating success (you can customize this as needed)
        return jsonify({"message": "Category received successfully."}), 200
    categories_data = db_controller.db.categories.find({})
    small_header_data, header_data, hero_data, sections_data = fetch_data()

    return render_template("categories.html", categories=categories_data, header=header_data, hero=hero_data, small_header=small_header_data, sections=sections_data,)

