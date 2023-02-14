class uppercase(object):
    def __init__(self):
        self.s=""
    
    def string(self):
        self.s = input()
    
    def upper(self):
        print(self.s.upper())

s = uppercase()
s.string()
s.upper()