from classes import db

class Section(object):
    def __init__(self, name=None, categories=None):
        self.name = name
        self.categories = categories

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
            if categories:
                self.categories = categories
            db.Insert(self)

    def add_category(self, section, category):
        self.name = section
        x = db.Select(self)[0]

        if x:
            c = x["categories"]
            c.append(category)
            temp = Section(x["name"],c)
            db.Update(self, temp)

    def update_category_name(self, section, category, newcategory):
        self.name = section
        x = db.Select(self)[0]

        if x:
            c = x["categories"]
            if category in c:
                i = c.index(category)
                c[i] = newcategory

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
