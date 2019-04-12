class rectangle:
    height, width = 0, 0

    def area(self):
        return self.height * self.width
    

    def __init__(self, x, y):
        self.set_size(x,y)


    def set_size(self, x, y):
        self.width, self.height = x, y
    


r = rectangle(5,4)
print(r.area())
r.set_size(9,4)
print(r.area())
