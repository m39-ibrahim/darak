from classes import db
#ask about the recipt class
class Section(object):
    def __init__(self, id,name=None, categories=None):
        self.id =""
        self.name = name
        self.categories = categories
        
    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value
        
        
    def get_all_sections(self):
        return db.Select(Section())

    def get_categories(self, section, withitems = False):
        x = db.Select(Section(section))[0]

        if x:
            temp = []
            if withitems:
                for cat in x["categories"]:
                    items = db.Select(Item(section=section, category = cat))
                    c = {
                        "name":cat,
                        "items":items
                         }
                    temp.append(c)
            else:
                for cat in x["categories"]:
                    temp.append(cat)
        return temp

    def add_section(self, name, categories = None):
        if db.Select(Section(name)):
            print("Error: Section already exists")
        else:
            self.name = name
            if categories: #if categpries provided
                self.categories = categories
            db.Insert(self) #inserts the current instance into the database
     
    def update_section_name(self, current_name, new_name):
        # Query the database to check if the section with the current_name exists
        existing_section = db.Select(Section(current_name))
        
        if existing_section:
            # Update the section's name
            existing_section[0]["name"] = new_name
            
            # Update the section in the database
            db.Update(Section(current_name), existing_section[0])
        else:
            print("Error: Section not found")
            
    def delete_section(self, name):
        db.Delete(Section(name))
        

    def add_category(self, section, category): #This line assigns the section parameter (the name of the section to which the category should be added) to the name attribute
        self.name = section
        x = db.Select(self)[0] # This line selects a record from the database that matches the section's name, represented by the instance. It then stores the result in x. [0] is used to access the first result (assuming there's only one matching record).

        if x:#check if a matching section was found
            c = x["categories"]
            c.append(category)
            temp = Section(x["name"],c) #After updating the list of categories, a new Section object is created with the same section name (x["name"]) and the modified list of categories (c).
            db.Update(self, temp)

    def update_category_name(self, section, category, newcategory):
        self.name = section
        x = db.Select(self)[0]

        if x: 
            c = x["categories"]
            if category in c:
                i = c.index(category)
                c[i] = newcategory #pdates the category name at index i with the new category name specified by the newcategory parameter.

                temp = Section(x["name"],c)
                db.Update(self, temp) #eates a new Section object with the updated list of categories, where x["name"] is the name of the section, and c is the updated list of categories.
            else:
                print("Error category not found in section")#
        
    def delete_category(self, section, category):
        self.name = section
        x = db.Select(self)[0]
        if x:
            c = x["categories"]
            if category in c:
                c.remove(category)
                temp = Section(x["name"],c)
                db.Update(self, temp)
            else:
                print("Error category not found in section")
    
    
class Item(object):
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__price = None
        self.__description = None
        self.__quantity = None

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value

    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value

    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, value):
        self.__quantity = value
        
   # def add_item(self, name, price, description, quantity):
        # self.name = name
        # self.price = price
        # self.description = description
        # self.quantity = quantity
        # db.Insert(self)
# you need to choose the category that you are going to add to and also add the rest of item functionalties here


class Reciept(object):
    def __init__(self):
        self.__reference = None
        self.__payment = None
        self.__date_and_time = None
        self.__delivery_or_pickup = None
        self.__price_before_discount = None
        self.__discount = None
        self.__payment = None

    def get_reference(self):
        return self.__reference

    def set_reference(self, value):
        self.__reference = value

    def get_payment(self):
        return self.__payment

    def set_payment(self, value):
        self.__payment = value

    def get_date_and_time(self):
        return self.__date_and_time

    def set_date_and_time(self, value):
        self.__date_and_time = value

    def get_delivery_or_pickup(self):
        return self.__delivery_or_pickup

    def set_delivery_or_pickup(self, value):
        self.__delivery_or_pickup = value

    def get_price_before_discount(self):
        return self.__price_before_discount

    def set_price_before_discount(self, value):
        self.__price_before_discount = value

    def get_discount(self):
        return self.__discount

    def set_discount(self, value):
        self.__discount = value
