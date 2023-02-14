class Square:
    def __init__(self, length ):
        self.length  = length

    def area (self):
        print(self.length * self.length == 0)  

class Shape(Square):
    def __init__(self, length = 0 ):
        self.length  = length
    
    def area (self) :
        print(self.length * self.length) 