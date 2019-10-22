import sys 



class maze():
    vec = ((0,1), (1,0), (0,-1), (-1,0))
    dir_vec = {(0,1) : ">", (1,0): "v", (0,-1): "<", (-1,0): "^"}
    def __init__(self, plan):
        self.plan = plan
        for i in range(len(plan)):
            for j in range(len(plan[0])):
                if plan[i][j] in "^>v<":
                    self.position = (i,j)
                    self.vector = (0,0)         # x, y
                    char = plan[i][j]
                    self.plan[i][j] = "."
                    if char == "^": self.vector = self.vec[3]
                    if char == ">": self.vector = self.vec[0]
                    if char == "v": self.vector = self.vec[1]
                    if char == "<": self.vector = self.vec[2]
                    return
        
    def print(self):
        for i in range(len(self.plan)):
            for j in range(len(self.plan[0])):
                if j != 0: print(" ", end="")
                if (i,j) == self.position: 
                    self.print_player()
                else:
                    print(self.plan[i][j], end="")
            # if i != len(self.plan) -1: print()
            print()

    def print_player(self):
        print(self.dir_vec[self.vector], end="")

    def turn_left(self):
        i = self.vec.index(self.vector)
        i = (i - 1) % 4
        self.vector = self.vec[i]

    def turn_right(self):
        i = self.vec.index(self.vector)
        i = (i + 1) % 4
        self.vector = self.vec[i]

    def move(self):
        x, y = self.position
        self.turn_right()
        x1, y1 = x + self.vector[0],y + self.vector[1]
        #print(self.vector)
        #print(f"{x1} / {y1}")
        while self.plan[x1][y1] == "#":
            self.turn_left()
            x1, y1 = x + self.vector[0],y + self.vector[1]
            #print(f">>{x1} / {y1}")

        self.position = (x1,y1) #move forvard

        


        



arr = []
count = int(sys.stdin.readline())
for line in sys.stdin:
    arr.append(line.split())
m = maze(arr)
#m.print()
for i in range(count):
    m.move()
m.print()
