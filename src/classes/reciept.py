from classes.payment import Payment


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
