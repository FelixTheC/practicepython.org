#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import json

class Birthday:
    
    birthDic = {}
    
    def __init__(self):
        self.read_file()
    
    def __str__(self, name, date):
        return(name + " " + date)        
        
    def read_file(self, jsonFile="birthday.json"):
        try:
            with open(jsonFile, 'r+') as f:
                self.birthDic = json.load(f) 
        except FileNotFoundError:
            return None

    def save(self, jsonFile):
        with open(jsonFile, "w") as f:
            json.dump(self.birthDic , f)


    def get_birthday_by_name(self, name):
        date = self.birthDic.get(name, 'no birthday data found')
        return self.__str__(name, date)


    def create_birthday(self, name, birthdayString):
        try:
            self.birthDic[name] = birthdayString
            return True
        except:
            return False
    
