class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self):
        self.x2=int(input())
        self.y2=int(input())

    def dist(self):
        print(((self.x2-self.x)**2+(self.y2-self.y)**2)**0.5)

x1=int(input())
y1=int(input())
poi=Point(x1,y1)
poi.show()
poi.move()
poi.dist()