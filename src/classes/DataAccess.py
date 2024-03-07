from pymongo import MongoClient

class DatabaseController():
    def __init__(self):
        uri = "mongodb+srv://m39-ibrahim:Engmahdy2003@cluster0.zmiw6ok.mongodb.net/"
        self.client = MongoClient(uri)
        self.db = self.client.darak
        self.tables = {
        "User":self.db.user,
        }

    def Insert(self, element):
        table = self.tables[element.__class__.__name__]
        table.insert_one(element.__dict__)

    def Select(self, query):
        # Directly assume query is a dictionary for simplicity
        table = self.tables['User']  # Direct reference to the User collection
        cursor = list(table.find(query))
        print(cursor)
        return cursor


    def Update(self,element,newElement):
        table = self.tables[str(type(element))]
        self.cursor = table.find_one_and_update(element.__dict__,{"$set":newElement.__dict__})

    def Delete(self,element):
        table = self.tables[str(type(element))]
        self.cursor = table.delete_many(element.__dict__)