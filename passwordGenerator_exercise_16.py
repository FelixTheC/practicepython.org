#! /usr/env/python3

class PwdGen():
    from random import choice
    
    def __init__(self):
        import string
        self.lower = string.ascii_lowercase
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.mix = string.hexdigits
        self.symb = ['#','!','_','-','$','&','?','*',' ']
        self.pwd = ''
        self.pwdList = []
        
    def __call__(self):
        return {'weak':self.weak(),
                'middle':self.middle(),
                'strong':self.strong()}
        
    def weak(self, choice=choice):
        if len(self.pwdList) > 0:
            self.pwdList.clear()
            self.pwd = ''
        self.pwdList = self.pwdList
        for i in range(6):
            self.pwdList.append(choice(self.lower))
        return self.pwd.join(self.pwdList)
    
    def middle(self, choice=choice):
        if len(self.pwdList) > 0:
            self.pwdList.clear()
            self.pwd = ''
        for i in range(8):
            self.pwdList.append(choice(self.letters))
        return self.pwd.join(self.pwdList)
    
    def strong(self, choice=choice):
        from random import randint
        strong = self.mix
        if len(self.pwdList) > 0:
            self.pwdList.clear()
            self.pwd = ''

        for i in range(16):
            if i % randint(2,3) == 0:
                self.pwdList.append(choice(self.symb))
            self.pwdList.append(choice(strong))
        for item in self.pwdList:
            self.pwd += str(item)
        return self.pwd    
    

if __name__ == "__main__":
    pwd = PwdGen()
    print(pwd())
    weak = pwd()['weak']
    print(weak)
    print(pwd.weak())
                
    