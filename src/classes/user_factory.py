from classes.admin import Admin
from classes.customer import Customer
from classes.manager import manager
# login related
class UserFactory(object):
    @staticmethod
    def get_user_type(t: str):
        types = {"admin": Admin,
                 "customer": Customer,
                 "manager": manager}

        if t not in types:
            raise Exception("%s competition type does not exist" % type)

        return types[t]
