# category.py
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from classes.DataAccess import DatabaseController
from home import fetch_data
from flask import session

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
    # print("Category name:", category_name,".")
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
    # print(items_data)
    categories_data = db_controller.db.categories.find({})
    small_header_data, header_data,hero_data, sections_data = fetch_data()
    fav = []
    if "email" in session:
        user_email = session.get('email')
        user_favorite = db_controller.db.favorites.find_one({'user_email': user_email})
        if user_favorite:
            for item in user_favorite.get('items', []):
                fav.append(str(item))

    cart = []
    if "email" in session:
        user_email = session.get('email')
        user_cart = db_controller.db.cart.find_one({'user_email': user_email})
        if user_cart:
            for item in user_cart.get('items', []):
                cart.append(str(item))
    # Render the template with the category title and items data
    return render_template("categories.html", carted=cart,category_title=category_name, items=items_data, favorited=fav, categories=categories_data, header=header_data,  hero_data = db_controller.db.hero.find_one(), small_header=small_header_data, sections=sections_data)

# @category_bp.route("/toggle_favorite", methods=["POST"])
# def toggle_favorite():
#     if request.method == "POST":
#         # Extract the item ID from the request data
#         item_id = request.form.get("item_id")

#         # Perform the logic to toggle the item in favorites (add/remove)
#         # This could involve updating the user's favorites in the database

#         # For now, let's just print the item ID to confirm it's received correctly
#         print("Toggling favorite for item ID:", item_id)

#         # Return a JSON response indicating success
#         return jsonify({"message": "Item toggled in favorites successfully"}), 200
#     else:
#         # Return a JSON response indicating method not allowed
#         return jsonify({"error": "Method not allowed"}), 405

@category_bp.route("/toggle_favorite", methods=["POST"])
def toggle_favorite():
    if request.method == "POST":
        # Extract the item ID from the request data
        item_id = request.form.get("item_id")
        # print("Item ID:", item_id)

        # Retrieve user email from session
        user_email = session.get('email')

        # Check if the user is logged in
        if not user_email:
            return jsonify({"error": "User not logged in"}), 401

        # Check if the item is already in favorites for the user
        user_favorite = db_controller.db.favorites.find_one({'user_email': user_email})

        if user_favorite and item_id in user_favorite.get('items', []):
            # Item is already in favorites, remove it
            db_controller.db.favorites.update_one(
                {'user_email': user_email},
                {'$pull': {'items': item_id}}
            )

            return jsonify({"message": "Item removed from favorites successfully"}), 200
        else:
            # Item is not in favorites, add it
            db_controller.db.favorites.update_one(
                {'user_email': user_email},
                {'$addToSet': {'items': item_id}},
                upsert=True
            )

            return jsonify({"message": "Item added to favorites successfully"}), 200
    else:
        return jsonify({"error": "Method not allowed"}), 405

