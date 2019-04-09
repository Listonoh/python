"""
zkouska nice
"""

import os

_A = "nic"

FILE = "c.txt"

MUJ_FILE = open(FILE, mode="a+")

print(MUJ_FILE)
MUJ_FILE.write("ahoj")

MUJ_FILE.close()

MUJ_FILE = open(FILE, mode="r")

fl = MUJ_FILE.readlines()
for x in fl:
    print(x)
print(os.getcwd())

MUJ_FILE.close()
