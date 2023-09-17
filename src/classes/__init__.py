from classes import DataAccess

try:
    db  = DataAccess.DatabaseController()
except:
    print("Error Connecting to database, please check your connection.")
    
