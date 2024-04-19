from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for
from classes.DataAccess import DatabaseController
from flask_login import login_required
from main import app
from home import fetch_data
from bson import ObjectId

cart_bp = Blueprint('cart', __name__)
db_controller = DatabaseController()

# @app.route('/cart', methods=['GET'])
@cart_bp.route('/cart', methods=['GET'])
def cart():
    # Retrieve user email from session
    user_email = session.get('email')
    if not user_email:
        # Redirect to login if user is not logged in
        return redirect(url_for('login'))
    
    # Fetch data for header, hero, small_header, and sections
    small_header_data, header_data, hero_data, sections_data = fetch_data()
    
    # Initialize an empty list to store item data
    items_data = []

    # Retrieve user cart items
    user_cart = db_controller.db.cart.find_one({'user_email': user_email})
    if user_cart:
        # Retrieve item IDs from user's cart
        item_ids = user_cart.get('items', [])
        
        # Convert item IDs from strings to ObjectId
        item_object_ids = [ObjectId(item_id) for item_id in item_ids]

        total_price = 0  # Initialize total price
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
                total_price += item_data['price']
                # print(f"Item with ID {item_id} found.")
            else:
                print(f"Item with ID {item_id} not found.")
    fav = []
    if "email" in session:
        user_email = session.get('email')
        user_favorite = db_controller.db.favorites.find_one({'user_email': user_email})
        if user_favorite:
            for item in user_favorite.get('items', []):
                fav.append(str(item))

    # Pass the items and other data to the template
    return render_template('cart.html',total_price=total_price,favorited=fav, items=items_data, header=header_data, hero_data=hero_data, small_header=small_header_data, sections=sections_data)

@cart_bp.route('/add_to_cart', methods=['POST'])
# @login_required
def add_to_cart():
    # Retrieve user email from session
    user_email = session.get('email')
    if not user_email:
        return jsonify({'error': 'User email not found in session'}), 401

    # Retrieve item_id from the request form
    item_id = request.form.get('item_id')

    # Check if user already has a cart
    user_cart = db_controller.db.cart.find_one({'user_email': user_email})

    if user_cart:
        # User already has a cart, update it
        db_controller.db.cart.update_one(
            {'user_email': user_email},
            {'$addToSet': {'items': item_id}}
        )
    else:
        # User does not have a cart, create a new one
        db_controller.db.cart.insert_one({
            'user_email': user_email,
            'items': [item_id]
        })

    return jsonify({'message': 'Item added to cart successfully'})

@cart_bp.route('/toggle_cart', methods=["POST"])
def toggle_cart():
    if request.method == "POST":
        # Extract the item ID from the request data
        item_id = request.form.get("item_id")

        # Retrieve user email from session
        user_email = session.get('email')

        # Check if the user is logged in
        if not user_email:
            return jsonify({"error": "User not logged in"}), 401

        # Check if the item is already in the cart for the user
        user_cart = db_controller.db.cart.find_one({'user_email': user_email})

        if user_cart and item_id in user_cart.get('items', []):
            # Item is already in the cart, remove it
            db_controller.db.cart.update_one(
                {'user_email': user_email},
                {'$pull': {'items': item_id}}
            )

            return jsonify({"message": "Item removed from cart successfully"}), 200
        else:
            # Item is not in the cart, add it
            db_controller.db.cart.update_one(
                {'user_email': user_email},
                {'$addToSet': {'items': item_id}},
                upsert=True
            )

            return jsonify({"message": "Item added to cart successfully"}), 200
    else:
        return jsonify({"error": "Method not allowed"}), 405
