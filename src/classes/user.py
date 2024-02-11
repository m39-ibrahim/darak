from classes import db

# check if you are going to add password here or not
class User(object):
    def __init__(self, id, name, email, phone_number, address):
        self.__id = ""
        self.__name = ""
        self.__email =""
        self.__phone_number = ""
        self.__address = ""

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_email(self):
        return self.__email

    def set_email(self, value):
        self.__email = value

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, value):
        self.__phone_number = value

    def get_address(self):
        return self.__address

    def set_address(self, value):
        self.__address = value


    def add_user(self, id, name, email, phone_number, address):
        if db.select(User(id)):
            print("Error: Item already exists")
        else:
            self.name = name
            self.__email = email
            self.phone_number = phone_number
            self.address = address
            db.Insert(self)

    def delete_user(self, id):
        existing_user = db.Select(User(id))
        if existing_user:
            db.Delete(User(id))
        else:
            print("Error: Item not found")
   

        db.delete_user(self.get_id())

def update_user(self, id, new_name=None, new_email=None, new_phone_number=None, new_address=None):
    existing_user = db.Select(User(id))
    if existing_user:
        if new_name is not None:
            existing_user[0]["name"] = new_name
        if new_email is not None:
            existing_user[0]["email"] = new_email
        if new_phone_number is not None:
            existing_user[0]["phone_number"] = new_phone_number
        if new_address is not None:
            existing_user[0]["address"] = new_address

        db.update_user(existing_user[0])
    else:
        print("Error: User not found")
