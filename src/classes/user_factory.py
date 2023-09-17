from classes.admin import Admin
from classes.customer import Customer

class UserFactory(object):
    @staticmethod
    def get_user_type(t: str):
        types = {"admin": Admin,
                 "customer": Customer}

        if t not in types:
            raise Exception("%s competition type does not exist" % type)

        return types[t]
