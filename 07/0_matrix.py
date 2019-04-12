class matrix:

    def __init__(self, x=0,y=0):
        self.x, self.y = x, y
        self.val = [[0 for i in range(x)] for i in range(y)]
        print(self.val)

    
    def __modify__(self, x, y, to_value):
        self.val[x][y] = to_value

    
    def print(self):
        for i in self.val:
            for j in i:
                print(j, end = " ")
            print()


    def __add__(self, second):
        if self.x != second.x & self.y != second.y:
            raise ValueError()
        temp = matrix(self.x, self.y)
        for i in range(self.x):
            for j in range(self.y):
                temp.__modify__(i,j, self.val[i][j] + second.val[i][j])
        return temp


m = matrix(3,3)
m.__modify__(1,1,1)
m.print()
n = m + m
n.print()
