#-*-coding:utf8;-*-
#qpy:3
#qpy:console

class Birthday():
    import json
    
    def __init__(self):
        self.birthDic = self.readFile()
        if self.birthDic == None:
            self.birthDic = {}
    
    def __str__(self, name, date):
        print(name + " " + date)        
        
    def readFile(self):
        try:
            with open("birthday.json", 'r+') as f:
                return self.json.load(f) 
        except:
            return None

    def save(self):
        with open("birthday.json", "w") as f:
            self.json.dump(self.birthDic , f)


    def getBirthdayByName(self, name):
        date = self.birthDic.get(name, 'no birthday data found')
        return self.__str__(name, date)


    def createBirthday(self, name, birthdayString):
        try:
            self.birthDic[name] = birthdayString
            return True
        except:
            return False
    
