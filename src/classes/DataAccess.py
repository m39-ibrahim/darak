from pymongo import MongoClient

class DatabaseController():
    def __init__(self):
        uri = "mongodb+srv://m39-ibrahim:Engmahdy2003@cluster0.zmiw6ok.mongodb.net/"
        self.client = MongoClient(uri)
        self.db = self.client.darak
        self.tables = {
        "User":self.db.user,
        "Section":self.db.section,
        }

    def Insert(self, element):
        table = self.tables[element.__class__.__name__]
        table.insert_one(element.__dict__)

    def Select(self, query):
        table = self.tables['User']
        cursor = list(table.find(query))
        return cursor


    def Update(self,element,newElement):
        table = self.tables[str(type(element))]
        self.cursor = table.find_one_and_update(element.__dict__,{"$set":newElement.__dict__})

    def Delete(self,element):
        table = self.tables[str(type(element))]
        self.cursor = table.delete_many(element.__dict__)
        
    def get_categories(self):
        section_table = self.tables['Section']
        categories = []
        sections = section_table.find({}, {'categories': 1})
        for section in sections:
            categories.extend(section['categories'])
        return categories