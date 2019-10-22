class rectangle:
    height, width = 0, 0

    def area(self):
        return self.height * self.width
    

    def __init__(self, x, y):
        self.set_size(x,y)


    def __eq__(self, oter):
        return self.area() == oter.area()

    def __lt__(self, oter):
        return self.area() < oter.area()

    
    def __le__(self, oter):
        return self.area() <= oter.area()

    def __gt__(self, oter):
        return self.area() > oter.area()

    
    def __ge__(self, oter):
        return self.area() >= oter.area()

    def set_size(self, x, y):
        self.width, self.height = x, y
    


r = rectangle(5,4)
d = rectangle(4,9)
r.set_size(9,4)

print(r<d)
print(r<=d)
print(r>d)
print(r>=d)
print(r==d)
print(r.area())
