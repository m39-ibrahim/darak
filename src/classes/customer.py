from classes.user import User


class Customer(User):
    def __init__(self, name, email, phone_number, address):
        super().__init__( name, email, phone_number, address)
