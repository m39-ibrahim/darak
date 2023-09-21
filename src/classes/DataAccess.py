from pymongo import MongoClient

class DatabaseController():
    def __init__(self):
        uri = "mongodb+srv://m39-ibrahim:<password>@cluster0.zmiw6ok.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(uri)
        self.db = self.client.darak_mall
        self.tables = {
        # "<class 'classes.Structures.City'>":self.db.Cities,
        # "<class '__main__.Listing'>":self.db.Listings,
        }

    def Insert(self, element):
        table = self.tables[str(type(element))]
        self.cursor = table.insert_one(element.__dict__)

    def Select(self, element):
        table = self.tables[str(type(element))]
        cursor=list(table.find(element.__dict__))
        if len(cursor) == 0:
            self.cursor = [None]
        else:
            self.cursor = cursor

        return self.cursor

    def Update(self,element,newElement):
        table = self.tables[str(type(element))]
        self.cursor = table.find_one_and_update(element.__dict__,{"$set":newElement.__dict__})

    def Delete(self,element):
        table = self.tables[str(type(element))]
        self.cursor = table.delete_many(element.__dict__)
