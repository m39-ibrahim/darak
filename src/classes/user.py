from classes import db


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
