from classes.user import User


class Admin(User):
    def __init__(self,id, name, email, phone_number, address):
        super().__init__(id, name, email, phone_number, address)
