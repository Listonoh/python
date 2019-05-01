#!/usr/bin/env python3
"""
justyfy 
"""

import sys

class buffer:
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.eop = False
        self.buf = []

    def add(self, word):
        if self.size + len(word) > self.max_size:
            self.flush()
        self.buf.append(word)
        self.size += len(word) + 1

    def flush(self, end_of_parg = False):
        if self.size == 0: return
        if self.eop: 
            self.eop = False 
            print("")
        if not end_of_parg:
            if len(self.buf) > 1:
                n, m = divmod(self.max_size - self.size + 1, len(self.buf) - 1)
                narrow, wide = " "*(n+1), " "*(n+2)
                print(wide.join(self.buf[:m] + [narrow.join(self.buf[m:])]))
            else: #only one item in list
                print(self.buf[0])
        else:
            print(" ".join(self.buf))
            self.eop = True
        self.buf = []
        self.size = 0



if len(sys.argv) != 2 or not sys.argv[1].isnumeric() or int(sys.argv[1]) < 1: 
    exit()

if __name__ == "__main__":
    buffer = buffer(int(sys.argv[1]))
    for line in sys.stdin:
        if line.strip() == "":
            buffer.flush(True)
        else:
            for word in line.split():
                buffer.add(word)
    buffer.flush(True)

