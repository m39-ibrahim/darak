from flask import Blueprint, render_template, request, session
from classes.DataAccess import DatabaseController
from home import fetch_data
from fuzzywuzzy import fuzz

search_bp = Blueprint('search', __name__)
db_controller = DatabaseController()

@search_bp.route("/search", methods=["GET"])
def search():
    # Get the search query from the request
    query = request.args.get("query")
    print("Search query:", query)

    # Split the query into individual words
    query_words = query.split()

    # Perform the search in the database
    items = db_controller.db.item.find({})

    # Prepare a list to store item data
    items_data = []

    # Iterate through each item fetched from the database
    for item in items:
        # Calculate fuzzy match scores for section, category, name, and description
        section_score = max(fuzz.partial_ratio(word.lower(), item["section"].lower()) for word in query_words)
        category_score = max(fuzz.partial_ratio(word.lower(), item["category"].lower()) for word in query_words)
        name_score = max(fuzz.partial_ratio(word.lower(), item["name"].lower()) for word in query_words)
        description_score = max(fuzz.partial_ratio(word.lower(), item["description"].lower()) for word in query_words)

        # Decide a threshold score for considering a match
        threshold = 70  # Adjust this threshold based on your requirements

        # If any score is above the threshold, consider it a match
        if any(score >= threshold for score in [section_score, category_score, name_score, description_score]):
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
            print(item_data)

    small_header_data, header_data, hero_data, sections_data = fetch_data()
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

    # Render the template with the search results
    return render_template("search.html", items=items_data, carted=cart, header=header_data, hero_data=db_controller.db.hero.find_one(), small_header=small_header_data, sections=sections_data)
