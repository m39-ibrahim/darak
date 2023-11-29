from classes import db

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

def update_company(self, name, new_name=None, email=None, new_email=None, phone_number=None, new_phone_number=None, address=None, new_address=None, social_media=None, new_social_media=None):

        existing_company = db.Select(Company(name))
        if existing_company:
            if new_name is not None:
                existing_company[0]["name"] = new_name
            if new_email is not None:
                existing_company[0]["email"] = new_email
            if new_phone_number is not None:
                existing_company[0]["phone_number"] = new_phone_number
            if new_address is not None:
                existing_company[0]["address"] = new_address
            if new_social_media is not None:
                existing_company[0]["social_media"] = new_social_media

            db.Update(Company(name), existing_company[0])
        else:
            print("Error: Company not found")

#EXAMPLE USAGE update_company("company_name", new_email="new_email@example.com", new_social_media=["new_twitter", "new_linkedin"])
