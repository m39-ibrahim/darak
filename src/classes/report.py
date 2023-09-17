from item import Item


class Report(object):
    def __init__(self):
        self.__item = []

    def get_item(self):
        return self.__item

    def set_item(self, value):
        self.__item = value
