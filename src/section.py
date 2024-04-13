# section.py
from flask import Blueprint, render_template, jsonify, request
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
    
    pprint(items_data)
    categories_data = db_controller.db.categories.find({})
    small_header_data, header_data,hero_data, sections_data = fetch_data()
    # Render the template with the section title and items data
    return render_template("sections.html", section_title=section_name, items=items_data, categories=categories_data, header=header_data,  hero_data=db_controller.db.hero.find_one(), small_header=small_header_data, sections=sections_data)
