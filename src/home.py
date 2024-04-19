from main import app
from flask import render_template
from classes.DataAccess import DatabaseController
from flask import request, jsonify, session
import random

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
    # Fetch last 4 items
    last_4_items = fetch_last_4_items()
            # Fetch 8 random items
    random_items = fetch_random_items()
    
    # Fetch user favorites and cart items
    fav = []
    cart = []
    if "email" in session:
        user_email = session.get('email')
        user_favorite = db_controller.db.favorites.find_one({'user_email': user_email})
        if user_favorite:
            for item in user_favorite.get('items', []):
                fav.append(str(item))
        user_cart = db_controller.db.cart.find_one({'user_email': user_email})
        if user_cart:
            for item in user_cart.get('items', []):
                cart.append(str(item))
    
    # Fetch other necessary data
    small_header_data, header_data, hero_data, sections_data = fetch_data()
    
    # Render the template with all the fetched data
    return render_template("index.html", carted=cart, favorited=fav, header=header_data, hero=hero_data, small_header=small_header_data, sections=sections_data, last_4_items=last_4_items, random_items=random_items)

def fetch_last_4_items():
    # Retrieve the last 4 items added to the item collection
    last_4_items = db_controller.db.item.find().sort([("_id", -1)]).limit(4)
    # Initialize a list to store item data
    items_data = []
    # Iterate through the last 4 items
    for item in last_4_items:
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

    return items_data


def fetch_random_items():
    # Retrieve a random sample of 8 items from the item collection
    random_items = db_controller.db.item.aggregate([{ '$sample': { 'size': 8 } }])
    
    # Initialize a list to store item data
    items_data = []

    # Iterate through the random items
    for item in random_items:
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

    return items_data

# About us route
@app.route("/about_us")
def about_us():
    small_header_data, header_data, hero_data, sections_data = fetch_data()
    return render_template("about_us.html", header=header_data, hero=hero_data, small_header=small_header_data, sections=sections_data)
