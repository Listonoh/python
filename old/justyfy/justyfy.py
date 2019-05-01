#!/usr/bin/env python3
"""
justyfy 
"""

import sys

class buffer:
    buf = []
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.eop = False

    def add(self, word):
        if self.size + len(word) > self.max_size:
            self.flush()
        self.buf.append(word)
        self.size += len(word) + 1

    def flush(self, end_of_parg = False):
        if self.size == 0: return

        if self.eop:
            self.eop = False
            print()
            

        if not end_of_parg:
            if len(self.buf) > 1:
                free_spaces = self.max_size - self.size + 1
                #print(self.buf)
                n, m = divmod(free_spaces, len(self.buf) - 1)
                narrow, wide = " "*(n+1), " "*(n+2)
                if m == 0:
                    print(narrow.join(self.buf))
                else:
                    l= self.buf[:m]
                    k = [narrow.join(self.buf[m:])]
                    a = wide.join(l + k)
                    print(a)
            else: 
                print(self.buf[0])
        else:
            print(" ".join(self.buf))
            self.eop = True
        self.buf = []
        self.size = 0



if len(sys.argv) != 2: 
    exit()
x = sys.argv[1]

if not x.isnumeric(): 
    exit()

xn = int(x)
if xn < 1: 
    exit() 

if __name__ == "__main__":
    buffer = buffer(xn)
    for line in sys.stdin:
        if line.strip() == "":
            buffer.flush(True)
        else:
            for word in line.split():
                buffer.add(word)
    buffer.flush(True)

