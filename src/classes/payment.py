from classes.item import Item


class Payment(object):
    def __init__(self):
        self.__card_number = None
        self.__card_expiray_date = None
        self.__card_cvv = None
        self.__name_on_card = None
        self.__items_bought = None
        self.__item = None

    def get_card_number(self):
        return self.__card_number

    def set_card_number(self, value):
        self.__card_number = value

    def get_card_expiray_date(self):
        return self.__card_expiray_date

    def set_card_expiray_date(self, value):
        self.__card_expiray_date = value

    def get_card_cvv(self):
        return self.__card_cvv

    def set_card_cvv(self, value):
        self.__card_cvv = value

    def get_name_on_card(self):
        return self.__name_on_card

    def set_name_on_card(self, value):
        self.__name_on_card = value

    def get_items_bought(self):
        return self.__items_bought

    def items_bought(self, value):
        self.__items_bought = value
