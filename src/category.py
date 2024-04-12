# category.py
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from classes.DataAccess import DatabaseController
from home import fetch_data

category_bp = Blueprint('category', __name__)
db_controller = DatabaseController()

# @category_bp.route("/categories", methods=["GET", "POST"])
# def categories():
#     if request.method == "POST":
#         # Extract the selected category from the JSON data
#         selected_category = request.json.get("category")
#         # Perform actions with the selected category (e.g., store it in the database, process it, etc.)
#         # For now, let's just print it
#         print("Selected category:", selected_category)
#         # Return a JSON response indicating success (you can customize this as needed)
#         # return jsonify({"message": "Category received successfully."}), 200
#         return redirect(url_for('category.display_category', category_name=selected_category))

#     categories_data = db_controller.db.categories.find({})
#     small_header_data, header_data,hero_data, sections_data = fetch_data()

#     return render_template("categories.html", categories=categories_data, header=header_data,  hero_data = db_controller.db.hero.find_one(), small_header=small_header_data, sections=sections_data)

@category_bp.route("/categories/<category_name>")
def display_category(category_name):
    print("Category name:", category_name,".")
    items = db_controller.db.item.find({"category": category_name})

    # Prepare a list to store item data
    items_data = []
    # Iterate through each item fetched from the database
    for item in items:
        # Extract necessary fields for each item
        item_data = {
            "id": str(item["_id"]),  # Convert ObjectId to string
            "category": item["category"],
            "section": item["section"],
            "quantity": int(item["quantity"]),  # Convert to integer
            "description": item["description"],
            "name": item["name"],
            "price": (item["price"]),  # Convert to float and adjust for currency
            "images": item.get("images", ""),  # Get images if available, otherwise empty string
        }
        items_data.append(item_data)
    print(items_data)
    categories_data = db_controller.db.categories.find({})
    small_header_data, header_data,hero_data, sections_data = fetch_data()
    # Render the template with the category title and items data
    return render_template("categories.html", category_title=category_name, items=items_data, categories=categories_data, header=header_data,  hero_data = db_controller.db.hero.find_one(), small_header=small_header_data, sections=sections_data)