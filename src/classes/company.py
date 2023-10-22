from classes.section import Section


class Company(object):
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__phone_number = None
        self.__address = None
        self.__social_media = None
        self.__section = None

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

    def get_social_media(self):
        return self.__social_media

    def set_social_media(self, value):
        self.__social_media = value

    def add_section(self, name):
        #code to add a section name here
        ...

    def update_section_name(self, id, name):
        #code to update a section name here
        ...
