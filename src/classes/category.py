from classes.item import Item


class Category(object):
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__item = None

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def add_item(self, name, price, description, quantitiy):
        ...

    def delete_item(self, id):
        ...

    def update_item_name(self, id, name):
        ...

    def update_item_price(self, id, price):
        ...

    def update_item_description(self, id, descrition):
        ...

    def update_item_quantity(self, id, quantitiy):
        ...
