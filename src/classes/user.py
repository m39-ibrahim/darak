from classes import db


class User(object):
    def __init__(self, id, password):
        self.__id = id
        self.__name = None
        self.__email = None
        self.__phone_number = None
        self.__address = None
        self.__password = password

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

    def login(self):
        user_info = db.select(self)

        if user_info == [None]:
            return False

        self.__name = user_info["name"]
        self.__email = user_info["email"]
        self.__phone_number = user_info["phone_number"]
        self.__address = user_info["address"]

        return self
