from tinydb import TinyDB, Query
import requests

class DB:
    def __init__(self,path):
        self.db = TinyDB(path)
        self.base_url = "https://bacefap.pythonanywhere.com"

    def get_tables(self):
        """
        To get the list of all the tables in the database
        """
        response = requests.get(self.base_url + "/smartphone/brands")
        return response.json()
        
    def getPhone(self,brand,idx):
        """
        Return phone data by brand
        args:
            brand: str
        return:
            dict
        """
        response = requests.get(self.base_url + "/smartphone/" + brand + "/" + str(idx))
        return response.json()

    def get_phone_list(self,brand):
        """
        Return phone list
        """
        response = requests.get(self.base_url + '/smartphone/' + brand)
        return response.json()

# db = DB('db.json')
# print(db.get_phone_list('Apple'))
