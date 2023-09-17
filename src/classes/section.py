from category import Category


class Section(object):
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__category = None

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def add_category(self, name):
        ...

    def update_category_name(self, id, name):
        ...
