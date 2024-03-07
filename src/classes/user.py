from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# Assuming db is a PyMongo instance or similar
from classes import db

class User(UserMixin):
    def __init__(self, name, email, phone_number, address, password):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        if password:
            self.password_hash = generate_password_hash(password)
        else:
            self.password_hash = None

    def get_id(self):
        return self.email

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_user(self):
        if db.Select(self):
            print("Error: User already exists")
        else:
            db.Insert(self)

    def delete_user(email):
        result = db.users.delete_one({"email": email})
        if result.deleted_count == 0:
            print("Error: User not found")

    def update_user(email, new_name=None, new_phone_number=None, new_address=None):
        updates = {}
        if new_name:
            updates['name'] = new_name
        if new_phone_number:
            updates['phone_number'] = new_phone_number
        if new_address:
            updates['address'] = new_address

        result = db.users.update_one({"email": email}, {"$set": updates})
        if result.matched_count == 0:
            print("Error: User not found")
