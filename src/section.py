from flask import Blueprint, render_template, jsonify, request, session
from classes.DataAccess import DatabaseController
from home import fetch_data
from pprint import pprint 

section_bp = Blueprint('section', __name__)
db_controller = DatabaseController()

# You can keep the existing route for displaying the section content
@section_bp.route("/sections/<section_name>", methods=['GET', 'POST'])
def display_section(section_name):
    section_name = section_name.replace("_", " ")
    section_name = section_name[0].upper() + section_name[1:]
    print("Section name:", section_name)
    items = db_controller.db.item.find({"section": section_name})
    print(items)

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
    
    # pprint(items_data)
    categories_data = db_controller.db.categories.find({})
    small_header_data, header_data,hero_data, sections_data = fetch_data()
    fav = []
    if "email" in session:
        user_email = session.get('email')
        user_favorite = db_controller.db.favorites.find_one({'user_email': user_email})
        for item in user_favorite.get('items', []):
            fav.append(str(item))
    # Render the template with the section title and items data
    return render_template("sections.html", section_title=section_name, items=items_data, favorited=fav,categories=categories_data, header=header_data,  hero_data=db_controller.db.hero.find_one(), small_header=small_header_data, sections=sections_data)

# @section_bp.route("/toggle_favorite", methods=["POST"])
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

@section_bp.route("/toggle_favorite", methods=["POST"])
def toggle_favorite():
    if request.method == "POST":
        # Extract the item ID from the request data
        item_id = request.form.get("item_id")
        print("Item ID:", item_id)

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

