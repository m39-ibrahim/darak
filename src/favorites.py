from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for
from classes.DataAccess import DatabaseController
from flask_login import login_required
from main import app
from home import fetch_data
from bson import ObjectId


favorites_bp = Blueprint('favorites', __name__)
db_controller = DatabaseController()

@app.route('/favorites', methods=['GET'])
def favorites():
    # Retrieve user email from session
    user_email = session.get('email')
    if not user_email:
        # Redirect to login if user is not logged in
        return redirect(url_for('login'))
    
    # Fetch data for header, hero, small_header, and sections
    small_header_data, header_data, hero_data, sections_data = fetch_data()
    
    # Initialize an empty list to store item data
    items_data = []

    # Retrieve user favorite items
    user_favorite = db_controller.db.favorites.find_one({'user_email': user_email})
    if user_favorite:
        # Retrieve item IDs from user's favorites
        item_ids = user_favorite.get('items', [])
        
        # Convert item IDs from strings to ObjectId
        item_object_ids = [ObjectId(item_id) for item_id in item_ids]
        print(f"Item ObjectIds: {item_object_ids}")

        # Retrieve the actual items from the database using the ObjectIds
        for item_id in item_object_ids:
            item = db_controller.db.item.find_one({'_id': item_id})
            if item:
                # Extract necessary fields for each item
                item_data = {
                    "id": str(item["_id"]),  # Convert ObjectId to string
                    "category": item["category"],
                    "section": item["section"],
                    "quantity": int(item["quantity"]),  # Convert to integer
                    "description": item["description"],
                    "name": item["name"],
                    "price": float(item["price"]),  # Convert to float and adjust for currency
                    "images": item.get("images", ""),  # Get images if available, otherwise empty string
                }
                # Append item data to the list
                items_data.append(item_data)
                print(f"Item with ID {item_id} found.")
            else:
                print(f"Item with ID {item_id} not found.")

    # Pass the items and other data to the template
    return render_template('favorites.html', items=items_data, header=header_data, hero_data=hero_data, small_header=small_header_data, sections=sections_data)


@favorites_bp.route('/add_to_favorites', methods=['POST'])
# @login_required
def add_to_favorites():
    # Debug: Print a message to indicate the beginning of the function
    # print("Add to favorites route called.")

    # Retrieve user email from session
    user_email = session.get('email')
    if not user_email:
        # Debug: Print an error message if user email is not found in session
        # print("Error: User email not found in session.")
        return jsonify({'error': 'User email not found in session'}), 401

    # Retrieve item_id from the request form
    item_id = request.form.get('item_id')

    # Check if user already exists in favorites collection
    user_favorite = db_controller.db.favorites.find_one({'user_email': user_email})

    if user_favorite:
        # Debug: Print a message to indicate that the user already exists in favorites collection
        # print("User already exists in favorites collection. Updating favorites...")

        # User already exists, update favorites
        db_controller.db.favorites.update_one(
            {'user_email': user_email},
            {'$addToSet': {'items': item_id}}
        )
    else:
        # Debug: Print a message to indicate that the user does not exist in favorites collection
        # print("User does not exist in favorites collection. Creating new document...")

        # User does not exist, create new document
        db_controller.db.favorites.insert_one({
            'user_email': user_email,
            'items': [item_id]
        })

    # Debug: Print a success message after adding the item to favorites
    # print("Item added to favorites successfully.")

    return jsonify({'message': 'Item added to favorites successfully'})

@favorites_bp.route('/favorites')
def favorites_page():
    # Render the favorites.html template
    return render_template('favorites.html')

@favorites_bp.route('/toggle_favorite', methods=["POST"])
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

