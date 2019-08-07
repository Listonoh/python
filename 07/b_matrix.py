class matrix:

    def __init__(self, x=0,y=0):
        self.x, self.y = x, y
        self.val = [[0 for i in range(x)] for i in range(y)]

    
    def __modify__(self, x, y, to_value):
        self.val[x][y] = to_value

    
    def print(self):
        print(self)
        for i in self.val:
            for j in i:
                print(j, end = " ")
            print()

    def init_thru_matrix(self, lis):
        self.x, self.y = len(lis[0]), len(lis)
        self.val = [[lis[i][j] for j in range(self.x)] for i in range(self.y)]
        return self

    def __add__(self, second):
        if self.x != second.x & self.y != second.y:
                raise ValueError()

        temp = matrix(self.x, self.y)

        for i in range(self.x ):
            for j in range(self.y):
                temp.__modify__(i,j, self.val[i][j] + second.val[i][j])
        return temp


        def __eq_(self, second):
            if self.x != second.x & self.y != second.y:
                return False

        for i in range(self.x ):
            for j in range(self.y):
                if self.val[i][j] != second.val[i][j]:
                    return False
        return True

    def __mul__(self, second):
        if self.x != second.y & self.y != second.y:
                raise ValueError()
        result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*second.val)] for A_row in self.val]

        return matrix().init_thru_matrix(result)
            
    #
    def __rmul__(self, numb): 
        result = [[self.val[i][j] * numb for j in range(self.x)] for i in range(self.y)]
        return matrix().init_thru_matrix(result)

    def __radd__(self, numb): 
        result = [[self.val[i][j] + numb for j in range(self.x)] for i in range(self.y)]
        return matrix().init_thru_matrix(result)

m = matrix(3,3)
m.__modify__(1,1,1)
m.print()
n = m + m
n.print()

A = [[12, 7, 3], 
    [4, 5, 6], 
    [7, 8, 9]] 

# take a 3x4 matrix 
B = [[5, 8, 1, 2], 
    [6, 7, 3, 0], 
    [4, 5, 9, 1]] 

# k == A
k = [[A[i][j] for j in range(len(A[i]))] for i in range(len(A))]

print(f"k> {k}")
print(f"A> {A}")

a1 = matrix()
a1.init_thru_matrix(A)

b1 = matrix()
b1.init_thru_matrix(B)

a1.print()
b1.print()

#from internet :) 
result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A] 
c1 = matrix().init_thru_matrix(result)
c1.print()

c1 = a1*b1
c1.print()

c1 = 2*c1
c1.print()
print(result) 